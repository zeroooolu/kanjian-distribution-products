from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
HTML_PATH = ROOT / '03-enterprise/prototype-v4/index.html'
CSS_PATH = ROOT / '03-enterprise/prototype-v4/styles.css'


def git_show(ref: str, path: str) -> str:
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'], text=True)


def page_span(html: str, page: str):
    marker = f'data-page="{page}"'
    main_start = html.index('<main>')
    pos = html.index(marker, main_start)
    start = html.rfind('<section class="page', main_start, pos)
    if start < 0:
        raise RuntimeError(f'page start not found: {page}')
    end = html.find('\n<section class="page', pos)
    if end < 0:
        end = html.index('\n</main>', pos)
    return start, end


def page_block(html: str, page: str) -> str:
    start, end = page_span(html, page)
    return html[start:end]


def replace_page(target: str, source: str, page: str) -> str:
    start, end = page_span(target, page)
    return target[:start] + page_block(source, page) + target[end:]


def filter_home_rule(line: str):
    if '[data-page="home"]' not in line or '{' not in line:
        return None
    prefix, rest = line.split('{', 1)
    indent = prefix[: len(prefix) - len(prefix.lstrip())]
    selectors = prefix.strip().split(',')
    selectors = [s.strip() for s in selectors if '[data-page="home"]' in s]
    if not selectors:
        return None
    return indent + ','.join(selectors) + '{' + rest


def home_only_extra(extra: str) -> str:
    lines = extra.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith(':root{--sonic') or stripped.startswith('.sonic-page{'):
            out.append(line)
            i += 1
            continue

        if stripped.startswith('@keyframes sonic-') or stripped.startswith('@media(prefers-reduced-motion:reduce)'):
            out.append(line)
            i += 1
            continue

        if stripped.startswith('@media(') and stripped.endswith('{'):
            media_head = line
            block = []
            i += 1
            depth = 1
            while i < len(lines) and depth:
                current = lines[i]
                st = current.strip()
                if st == '}':
                    depth -= 1
                    if depth == 0:
                        break
                elif st.startswith('@media(') and st.endswith('{'):
                    depth += 1
                filtered = filter_home_rule(current)
                if filtered:
                    block.append(filtered)
                i += 1
            if block:
                out.append(media_head)
                out.extend(block)
                out.append('}')
            i += 1
            continue

        filtered = filter_home_rule(line)
        if filtered:
            out.append(filtered)

        i += 1

    return '\n'.join(out).strip()


main_html = git_show('origin/main', '03-enterprise/prototype-v4/index.html')
main_css = git_show('origin/main', '03-enterprise/prototype-v4/styles.css')
current_html = HTML_PATH.read_text()
current_css = CSS_PATH.read_text()

# Keep the approved homepage experiment, but restore Product and Solutions exactly to main.
result_html = replace_page(current_html, main_html, 'product')
result_html = replace_page(result_html, main_html, 'solutions')

if page_block(result_html, 'product') != page_block(main_html, 'product'):
    raise RuntimeError('product page is not identical to main')
if page_block(result_html, 'solutions') != page_block(main_html, 'solutions'):
    raise RuntimeError('solutions page is not identical to main')

if not current_css.startswith(main_css):
    raise RuntimeError('preview styles are no longer main styles plus visual additions')
extra = current_css[len(main_css):]
home_css = home_only_extra(extra)
result_css = main_css.rstrip() + '\n\n/* Enterprise homepage visual experiment — homepage only */\n' + home_css + '\n'

if '[data-page="product"]' in home_css or '[data-page="solutions"]' in home_css:
    raise RuntimeError('non-home sonic selectors leaked into homepage-only CSS')
if 'capability-showcase' not in result_html or 'capability-showcase' not in result_css:
    raise RuntimeError('approved homepage capability visual is missing')
if 'sonic-product-hero' in page_block(result_html, 'product'):
    raise RuntimeError('product sonic markup still present')
if 'sonic-solutions-hero' in page_block(result_html, 'solutions'):
    raise RuntimeError('solutions sonic markup still present')

HTML_PATH.write_text(result_html)
CSS_PATH.write_text(result_css)
print('Prepared homepage-only enterprise visual preview; Product and Solutions restored from main.')

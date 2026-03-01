import re

def revert_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove SVG Defs
    svg_defs = """
    <svg width="0" height="0" class="svg-defs" style="position:absolute; width:0; height:0;">
        <defs>
            <linearGradient id="gradient-brand" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#EEFAAC" />
                <stop offset="50%" stop-color="#DDF469" />
                <stop offset="100%" stop-color="#B2C750" />
            </linearGradient>
        </defs>
    </svg>
    """
    html = html.replace(svg_defs, '')
    
    # 2. Replaces stroke="url(#gradient-brand)" with stroke="currentColor" 
    html = html.replace('stroke="url(#gradient-brand)"', 'stroke="currentColor"')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

def revert_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        css = f.read()

    css = css.replace('border: 1px solid rgba(221, 244, 105, 0.2);', 'border: 1px solid rgba(34, 197, 94, 0.2);')
    css = css.replace('box-shadow: 0 8px 25px rgba(221, 244, 105, 0.05);', 'box-shadow: 0 8px 25px rgba(34, 197, 94, 0.1);')
    css = css.replace('background: rgba(221, 244, 105, 0.06);', 'background: rgba(34, 197, 94, 0.08);')
    css = css.replace('border: 1px solid rgba(221, 244, 105, 0.15);', 'border: 1px solid rgba(34, 197, 94, 0.15);')
    css = css.replace('box-shadow: 0 0 20px rgba(221, 244, 105, 0.08); /* Dark glow */', 'box-shadow: 0 0 20px rgba(34, 197, 94, 0.08);')
    css = css.replace('filter: drop-shadow(0 0 6px rgba(221, 244, 105, 0.35));', 'filter: drop-shadow(0 0 4px rgba(34, 197, 94, 0.2));')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(css)

revert_html('index.html')
revert_css('style.css')

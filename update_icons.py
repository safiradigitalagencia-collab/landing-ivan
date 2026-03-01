import re

def update_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject SVG Defs right after <body> tag
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
    
    if "id=\"gradient-brand\"" not in html:
        html = html.replace('<body class="theme-light">', f'<body class="theme-light">\n{svg_defs}')
    
    # 2. Replaces stroke="currentColor" with stroke="url(#gradient-brand)" inside ALL SVG paths
    html = html.replace('stroke="currentColor"', 'stroke="url(#gradient-brand)"')
    
    # 3. Clean up style="color: var(--danger-red);" inside icon-check 
    html = html.replace('style="color: var(--danger-red);"', '')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

def update_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # Base color we are matching is rgba(221, 244, 105) for #DDF469
    # .icon-wrapper adjustments
    css = re.sub(
        r'border: 1px solid rgba\(34, 197, 94, 0\.2\);',
        r'border: 1px solid rgba(221, 244, 105, 0.2);',
        css
    )
    css = re.sub(
        r'box-shadow: 0 8px 25px rgba\(34, 197, 94, 0\.1\);',
        r'box-shadow: 0 8px 25px rgba(221, 244, 105, 0.05);',
        css
    )
    css = re.sub(
        r'filter: drop-shadow\(0 0 6px rgba\(34, 197, 94, 0\.2\)\);',
        r'filter: drop-shadow(0 0 8px rgba(221, 244, 105, 0.35)); /* Dark background subtle glow glow */',
        css
    )
    # dif-icon adjustments
    css = re.sub(
        r'background: rgba\(34, 197, 94, 0\.08\);',
        r'background: rgba(221, 244, 105, 0.06);',
        css
    )
    css = re.sub(
        r'border: 1px solid rgba\(34, 197, 94, 0\.15\);',
        r'border: 1px solid rgba(221, 244, 105, 0.15);',
        css
    )
    css = re.sub(
        r'box-shadow: 0 0 20px rgba\(34, 197, 94, 0\.08\);',
        r'box-shadow: 0 0 20px rgba(221, 244, 105, 0.08); /* Dark glow */',
        css
    )
    css = re.sub(
        r'filter: drop-shadow\(0 0 4px rgba\(34, 197, 94, 0\.2\)\);',
        r'filter: drop-shadow(0 0 6px rgba(221, 244, 105, 0.35));',
        css
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(css)

update_html('index.html')
update_css('style.css')

import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'(\.hero-video-wrapper\s*\{[^}]*margin:\s*0 auto )1\.25rem( auto;)',
    r'\g<1>60px\g<2>',
    css
)

if '.hero-transition-band' not in css:
    css += "\n\n/* Transition Band */\n.hero-transition-band {\n    height: 100px;\n    background: linear-gradient(to bottom, rgba(255,255,255,0), #f1f5f9 50%, #ffffff);\n    width: 100%;\n}\n"

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('</header>\n\n    <!-- 2. BLOQUE DE IDENTIFICACIÓN -->',
                    '</header>\n\n    <!-- TRANSITION BAND -->\n    <div class="hero-transition-band"></div>\n\n    <!-- 2. BLOQUE DE IDENTIFICACIÓN -->')

html = html.replace('<section class="problem section-dark text-center">',
                    '<section class="problem section-dark text-center" style="margin-top: 80px;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

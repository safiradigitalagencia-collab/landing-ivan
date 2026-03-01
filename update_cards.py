import sys

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the classes for the three pricing cards
html = html.replace('<!-- Plan 60 días -->\n                <div class="pricing-card secondary">',
                    '<!-- Plan 60 días -->\n                <div class="pricing-card secondary plan-card--60dias">')

html = html.replace('<!-- Plan 6 meses (Más elegido) -->\n                <div class="pricing-card featured">',
                    '<!-- Plan 6 meses (Más elegido) -->\n                <div class="pricing-card featured plan-card--6meses">')

html = html.replace('<!-- Plan anual (Mejor valor) -->\n                <div class="pricing-card secondary">',
                    '<!-- Plan anual (Mejor valor) -->\n                <div class="pricing-card secondary plan-card--anual">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Append CSS block to style.css
css_block = """
@media (max-width: 768px) {
    /* Set display grid or flex on the container if not already */
    .pricing-grid {
        display: flex !important;
        flex-direction: column !important;
    }
    
    .plan-card--60dias { order: 1 !important; }
    .plan-card--6meses { order: 2 !important; }
    .plan-card--anual  { order: 3 !important; }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_block)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

total_pattern = r'(    <!-- 11\. BLOQUE FAQ -->.*?    </section>\n)(\n)(    <!-- 12\. BLOQUE GARANTÍA -->.*?    </section>\n)'

def replacer(match):
    faq = match.group(1)
    sep = match.group(2)
    gar = match.group(3)
    
    faq = faq.replace('11. BLOQUE FAQ', '12. BLOQUE FAQ')
    gar = gar.replace('12. BLOQUE GARANTÍA', '11. BLOQUE GARANTÍA')
    
    return gar + sep + faq

new_content = re.sub(total_pattern, replacer, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

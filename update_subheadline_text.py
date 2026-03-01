import re

path = '/Users/amandaloba/pagina de vendas ivan/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Procura pela tag p com as classes específicas e substitui todo o seu conteúdo
pattern = r'<p class="hero-subtitle hero-subtitle-reorg">.*?</p>'
new_text = '<p class="hero-subtitle hero-subtitle-reorg">Un sistema estructurado para personas ocupadas que quieren reconstruir su disciplina, su cuerpo y la confianza en sí mismas</p>'

new_content = re.sub(pattern, new_text, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Subheadline updated successfully.")

import os

css_path = '/Users/amandaloba/pagina de vendas ivan/style.css'

css_to_add = """

/* --- ATUALIZACAO HERO (SUBHEADLINE) --- */
/* Desktop */
@media (min-width: 769px) {
    .hero-content h1, .hero-title {
        margin-bottom: 20px !important;
    }
    .hero-subtitle {
        font-size: 1.35rem !important; /* Fonte maior e mais elegível */
        max-width: 600px !important; /* Evita linhas muito longas */
        margin-bottom: 40px !important; /* Espaço até o vídeo */
        margin-left: auto !important;
        margin-right: auto !important;
        text-align: center !important;
        color: rgba(255, 255, 255, 0.95) !important;
        line-height: 1.6 !important;
    }
}

/* Mobile */
@media (max-width: 768px) {
    .hero-content h1, .hero-title {
        margin-bottom: 16px !important;
    }
    .hero-subtitle {
        font-size: 1.125rem !important; /* Aumenta a legibilidade mobile */
        max-width: 360px !important; /* Limite de largura no mobile */
        width: 90% !important;
        margin-top: 0 !important;
        margin-bottom: 32px !important; /* Espaço até o vídeo */
        margin-left: auto !important;
        margin-right: auto !important;
        text-align: center !important;
        color: rgba(255, 255, 255, 0.95) !important;
        line-height: 1.5 !important;
    }
}
"""

with open(css_path, 'a') as f:
    f.write(css_to_add)

print("CSS adicionado com sucesso.")

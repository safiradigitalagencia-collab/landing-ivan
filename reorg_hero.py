import re

html_path = '/Users/amandaloba/pagina de vendas ivan/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Substituição do Hero Content
# Vamos mirar do <h1 class="hero-title"> até o fechamento da <div class="hero-actions">
pattern = r'<h1 class="hero-title">Retoma el control\.<br>Vuelve al rigor\.</h1>.*?<div class="hero-actions">.*?</div>'

replacement_html = """<h1 class="hero-title hero-title-reorg">Tu mejor versión no desapareció.<br>Solo quedó enterrada bajo el caos.</h1>
            
            <div class="hero-play-badge">
                <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">
                    <path d="M8 5v14l11-7z"/>
                </svg>
                Mira el video y descubre cómo empezar
            </div>

            <div class="hero-video-wrapper">
                <iframe id="embed_vsl_hero"
                    src="https://www.youtube.com/embed/Umj3SHH425k?autoplay=1&mute=1&rel=0&modestbranding=1&showinfo=0&iv_load_policy=3&playsinline=1&controls=1&disablekb=1"
                    title="VSL Método 10 en 12"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    allowfullscreen>
                </iframe>
            </div>
            
            <p class="hero-subtitle hero-subtitle-reorg"><span class="text-highlight">El Método 10 en 12 es un sistema estructurado</span> para hombres que tuvieron disciplina física y quieren recuperar su seguridad y su presencia.</p>

            <div class="hero-actions hero-actions-reorg">
                <a href="#precio" class="btn btn-primary btn-large cta-button pulse-animation">EMPEZAR MI PROCESO</a>
            </div>"""

new_html = re.sub(pattern, replacement_html, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)


css_path = '/Users/amandaloba/pagina de vendas ivan/style.css'

css_append = """

/* --- RE-ORG HERO (Headline -> Badge -> Video -> Subheadline -> Botao) --- */
.hero-title-reorg {
    max-width: 800px !important;
    margin: 0 auto 1.5rem auto !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    line-height: 1.15 !important;
}

/* Badge do Video */
.hero-play-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: rgba(221, 244, 105, 0.1);
    color: #DDF469;
    padding: 8px 18px;
    border-radius: 50px;
    border: 1px solid rgba(221, 244, 105, 0.25);
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 2rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.hero-play-badge svg {
    flex-shrink: 0;
}

/* Espacamento do vídeo */
.hero-video-wrapper {
    margin-bottom: 2rem !important; /* Espaço entre vídeo e subheadline */
}

/* Nova Subheadline (Abaixo do Vídeo) */
.hero-subtitle-reorg {
    color: #FFFFFF !important;
    max-width: 650px !important;
    margin: 0 auto 2.5rem auto !important; /* 2.5rem pro botão respirar mais */
    font-size: 1.25rem !important;
    line-height: 1.6 !important;
    text-align: center !important;
}

/* Aumentando respiro acima do botāo se necessário, mas já resolvido pela margin-bottom da subheadline */
.hero-actions-reorg {
    margin-top: 0 !important;
}

/* MOBILE REFINEMENTS FOR REORG */
@media (max-width: 768px) {
    .hero-title-reorg {
        font-size: clamp(28px, 8vw, 36px) !important;
        margin-bottom: 1.25rem !important;
        max-width: 90% !important;
    }
    .hero-play-badge {
        font-size: 0.75rem;
        padding: 6px 14px;
        margin-bottom: 1.5rem;
    }
    .hero-subtitle-reorg {
        font-size: 1.125rem !important;
        max-width: 90% !important;
        margin-bottom: 2.5rem !important;
    }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_append)

print("Reorg done successfully.")

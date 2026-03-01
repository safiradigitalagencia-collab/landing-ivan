css_block = """
/* =========================================================
   AJUSTES FINAIS DE ESPAÇAMENTO DO HERO COMPACTO (Mobile + Desktop)
   ========================================================= */

/* DESKTOP HERO SPACINGS */
.hero {
    /* Diminuir preenchimento do topo do Hero (padding-top original era 120px ou mais) */
    padding-top: 60px !important;
    
    /* Espaço BOTAO -> PROXIMO BLOCO (Meta: 40-60px) */
    padding-bottom: 50px !important; 
    margin-bottom: 0px !important;
}

.hero-title {
    margin-bottom: 24px !important;
}

.hero-subtitle {
    margin-bottom: 32px !important;
}

.hero-video-wrapper {
    margin-bottom: 24px !important; /* Aproximar vídeo do botão no desktop também */
}

/* Remover espaço excessivo do segundo bloco */
.problem.section-dark {
    padding-top: 0px !important;
    margin-top: 0px !important;
}


/* MOBILE HERO SPACINGS */
@media (max-width: 768px) {
    .hero {
        /* TOP DO HERO -> HEADLINE mais curto */
        padding-top: 24px !important; 
        
        /* BOTAO -> PROXIMO BLOCO (Meta: 28-40px) */
        padding-bottom: 32px !important;
    }

    /* Garantir 2 linhas na Headline sem empilhar absurdamente */
    .hero-title {
        /* Aumentar para garantir q não suba do clamp de forma desengoçada, 
           mas o line-height 1.15 controla o visual e margin-bottom aperta o sub. */
        font-size: clamp(32px, 8vw, 40px) !important;
        line-height: 1.15 !important;
        margin-bottom: 16px !important; /* headline -> subheadline: 12-16px */
    }

    .hero-subtitle {
        margin-bottom: 24px !important; /* subheadline -> vídeo: 20-28px */
    }

    .hero-video-wrapper {
        margin-bottom: 20px !important; /* vídeo -> botão: 16-20px */
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_block)

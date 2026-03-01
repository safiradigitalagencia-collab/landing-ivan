import re

css = """
/* =========================================
   UX & TYPOGRAPHY STANDARDIZATION
   ========================================= */

/* Ensure globally all font families are clean */
h1, h2, h3, h4, h5, h6, .hero-title, .section-title, .card-title, .btn {
    font-family: 'Oswald', sans-serif !important;
}
p, span, li, a:not(.btn), div {
    font-family: 'Inter', sans-serif;
}

/* Fix inheritance inside buttons / spans */
.btn {
    font-family: 'Oswald', sans-serif !important;
}

/* 1. TYPOGRAPHIC SCALE - DESKTOP */
h1, .hero-title {
    font-size: 56px !important;
    line-height: 1.15 !important;
}
h2, .section-title {
    font-size: 36px !important;
    line-height: 1.2 !important;
}

/* Paragraph constraints */
p, .hero-subtitle, .pricing-subtitle, .solution-desc, .feature-subtitle, .feature-list-text span, .system-content-clean p, .solution-list li {
    font-size: 18px !important;
    line-height: 1.5 !important;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}
.text-left p, .text-left .feature-subtitle, .feature-list-text span {
    margin-left: 0;
    text-align: left;
}
.pricing-subtitle {
    margin-left: auto;
    margin-right: auto;
}

/* 2. STANDARDIZED SPACINGS - DESKTOP */
/* HERO */
.hero-title {
    margin-bottom: 24px !important;
}
.hero-subtitle {
    margin-bottom: 40px !important;
}
.hero-video-wrapper {
    margin-bottom: 32px !important;
}
/* Between button and next section: Desktop 70px */
.hero {
    padding-bottom: 70px !important;
}
.problem.section-dark {
    /* Set padding-top back to normal as spacing is handled by hero padding bottom */
    padding-top: 0px !important;
}

/* SEGUNDO BLOCO */
.problem.section-dark .section-title {
    margin-bottom: 20px !important;
}
.problem.section-dark .pricing-subtitle {
    margin-bottom: 30px !important;
}
.audience-col {
    padding: 28px !important;
}

/* BETWEEN SECTIONS */
.section-dark, .section-darker, .feature-section, .pricing, .faq, .guarantee, .cta-final {
    padding-top: 90px !important;
    padding-bottom: 90px !important;
}

/* Adjust problem section because of hero */
.problem.section-dark {
    padding-top: 0px !important;
}

/* 3. BUTTON STANDARDIZATION */
.btn {
    height: 56px !important;
    padding: 0 28px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-sizing: border-box !important;
}

/* =========================================
   UX & TYPOGRAPHY STANDARDIZATION - MOBILE
   ========================================= */
@media (max-width: 768px) {
    /* TYPOGRAPHIC SCALE - MOBILE */
    h1, .hero-title {
        font-size: 34px !important;
        line-height: 1.2 !important;
    }
    h2, .section-title {
        font-size: 26px !important;
        line-height: 1.25 !important;
    }
    p, .hero-subtitle, .pricing-subtitle, .solution-desc, .feature-subtitle, .feature-list-text span, .system-content-clean p, .solution-list li {
        font-size: 16px !important;
        line-height: 1.5 !important;
    }

    /* SPACINGS - MOBILE */
    /* HERO */
    .hero-title {
        margin-bottom: 16px !important;
    }
    .hero-subtitle {
        margin-bottom: 28px !important;
    }
    .hero-video-wrapper {
        margin-bottom: 24px !important;
    }
    .hero {
        padding-bottom: 50px !important;
    }
    .problem.section-dark {
        padding-top: 0px !important;
    }

    /* SEGUNDO BLOCO */
    .problem.section-dark .section-title {
        margin-bottom: 16px !important;
    }
    .problem.section-dark .pricing-subtitle {
        margin-bottom: 24px !important;
    }
    .audience-col {
        padding: 22px !important;
    }

    /* BETWEEN SECTIONS */
    .section-dark, .section-darker, .feature-section, .pricing, .faq, .guarantee, .cta-final {
        padding-top: 60px !important;
        padding-bottom: 60px !important;
    }
    .problem.section-dark {
        padding-top: 0px !important;
    }

    /* BUTTONS */
    .btn {
        height: 52px !important;
        padding: 0 24px !important;
    }

    /* TERCEIRO BLOCO (LA BASE DEL RENDIMIENTO) */
    .feature-grid {
        display: flex !important;
        flex-direction: column !important;
    }
    .feature-content-col {
        display: contents !important;
    }
    .feature-content-col > h2 {
        order: 1 !important;
        margin-bottom: 16px !important;
        text-align: center !important;
    }
    .feature-content-col > .feature-subtitle {
        order: 2 !important;
        margin-bottom: 32px !important;
        text-align: center !important;
        margin-left: auto;
        margin-right: auto;
    }
    .feature-image-col {
        order: 3 !important;
        margin-bottom: 32px !important;
    }
    .feature-content-col > .feature-list {
        order: 4 !important;
        margin-bottom: 32px !important;
    }
    .feature-content-col > .btn {
        order: 5 !important;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

# Update index.html inline style for section 2 background since we handle spacing natively now
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the hero padding bottom stretch into the beautiful gradient that existed before
# Or rather, modify the gradient so it flows properly. The hero has .overlay for gradient.
# Let's clean up index.html margin-top/padding-top inline style for .problem.section-dark
html = re.sub(
    r'<section class="problem section-dark text-center" style="padding-top: 140px; background: linear-gradient\(to bottom, #EEF2F7 0%, #FFFFFF 60%, #f8fafc 100%\);">',
    r'<section class="problem section-dark text-center" style="background: linear-gradient(to bottom, #EEF2F7 0%, #FFFFFF 60%, #f8fafc 100%);">',
    html
)

html = re.sub(
    r'<section class="problem section-dark text-center" style="margin-top: 80px;">',
    r'<section class="problem section-dark text-center" style="background: linear-gradient(to bottom, #EEF2F7 0%, #FFFFFF 60%, #f8fafc 100%);">',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS standardizations updated!")

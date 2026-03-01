import os

css_block = """
/* MOBILE ADJUSTMENTS */
@media (max-width: 480px) {
    /* 1) Hero Title */
    .hero-title {
        font-size: clamp(34px, 7.5vw, 46px) !important;
        line-height: 1.1 !important;
        letter-spacing: -0.02em !important;
    }

    /* 2) Background Gradient Recalibration */
    .overlay {
        background: linear-gradient(to bottom, #FFFFFF 0%, #F5F6F7 50%, #EEF2F6 100%) !important;
    }
    
    .problem.section-dark {
        background: linear-gradient(to bottom, #EEF2F6 0%, #FFFFFF 60%, #f8fafc 100%) !important;
    }

    /* 3) Button Below Video */
    .hero-actions .btn-primary {
        background: linear-gradient(180deg, #DDF469 0%, #CFEA55 100%) !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08) !important;
    }

    /* 4) Spacing */
    .hero-video-wrapper {
        margin-bottom: 32px !important;
    }

    .problem.section-dark {
        padding-top: 48px !important;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_block)

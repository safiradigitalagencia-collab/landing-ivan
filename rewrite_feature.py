import re

def rewrite_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    new_block = """    <!-- 9. BLOQUE DIFERENCIALES -->
    <section class="diferenciales feature-section section-darker">
        <div class="container">
            <div class="feature-grid">
                
                <!-- Columna Izquierda: Imagen -->
                <div class="feature-image-col">
                    <div class="feature-image-wrapper">
                        <!-- Placeholder: reemplazar 'assets/feature_placeholder.jpg' por la imagen real -->
                        <img src="assets/feature_placeholder.jpg" alt="App interface preview" style="width: 100%; height: 100%; object-fit: cover; border-radius: 24px;">
                    </div>
                </div>

                <!-- Columna Derecha: Contenido -->
                <div class="feature-content-col">
                    <h2 class="section-title text-left mb-2">La base del rendimiento</h2>
                    <p class="feature-subtitle text-muted mb-4" style="font-size: 1.1rem; max-width: 500px;">
                        Entrenamientos diseñados para resultados reales sin complicaciones. Todo lo que necesitas en la palma de tu mano.
                    </p>
                    
                    <ul class="feature-list" style="margin-bottom: 2.5rem;">
                        <li>
                            <div class="feature-list-icon">
                                <svg viewBox="0 0 24 24" fill="none" class="icon-gradient" stroke="url(#gradient-brand)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <!-- Icono de niveles (Barras) -->
                                    <line x1="12" y1="20" x2="12" y2="10"></line>
                                    <line x1="18" y1="20" x2="18" y2="4"></line>
                                    <line x1="6" y1="20" x2="6" y2="16"></line>
                                </svg>
                            </div>
                            <div class="feature-list-text">
                                <strong>Para todos los niveles</strong>
                                <span>Principiante o avanzado, cada sesión está pensada para desafiarte al ritmo adecuado.</span>
                            </div>
                        </li>
                        <li>
                            <div class="feature-list-icon">
                                <svg viewBox="0 0 24 24" fill="none" class="icon-gradient" stroke="url(#gradient-brand)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <!-- Icono de usuario (Equipamiento mínimo) -->
                                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="9" cy="7" r="4"></circle>
                                </svg>
                            </div>
                            <div class="feature-list-text">
                                <strong>Equipamiento mínimo</strong>
                                <span>Únete a una comunidad activa que crece mes a mes.</span>
                            </div>
                        </li>
                        <li>
                            <div class="feature-list-icon">
                                <svg viewBox="0 0 24 24" fill="none" class="icon-gradient" stroke="url(#gradient-brand)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <!-- Icono rayo (Rápido y eficiente) -->
                                    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                                </svg>
                            </div>
                            <div class="feature-list-text">
                                <strong>Rápido y eficiente</strong>
                                <span>Entrenamientos diseñados para dar resultados en menos tiempo. Entra, entrena y sigue con tu día.</span>
                            </div>
                        </li>
                    </ul>

                    <a href="#precio" class="btn btn-primary btn-large pulse-animation" style="padding: 18px 40px; border-radius: 50px;">Empezar Ahora</a>
                </div>

            </div>
        </div>
    </section>"""

    # Buscar el limite del bloque original 9 para reemplazarlo con re.sub
    pattern = r'<!-- 9\. BLOQUE DIFERENCIALES -->.*?</section>'
    html_new = re.sub(pattern, new_block, html, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_new)


def rewrite_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        css = f.read()

    new_css_block = """/* Feature Section Block (Substituindo antigo staggered grid) */
.feature-section {
    padding: 100px 0;
}

.feature-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
}

.feature-image-col {
    position: relative;
    width: 100%;
}

.feature-image-wrapper {
    background-color: #f1f5f9; /* Placeholder cinza clarinho / estético */
    border-radius: 24px;
    aspect-ratio: 4 / 4.5;
    position: relative;
    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08); /* Sombra elegante */
    overflow: hidden;
    border: 1px solid rgba(15, 23, 42, 0.05);
}

.feature-content-col {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.feature-subtitle {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 2.5rem;
    line-height: 1.6;
}

.feature-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.feature-list li {
    display: flex;
    align-items: flex-start;
    gap: 20px;
}

.feature-list-icon {
    width: 32px;
    height: 32px;
    flex-shrink: 0;
    margin-top: 4px;
    filter: drop-shadow(0 0 6px rgba(221, 244, 105, 0.4)); /* Glow suave */
}

.feature-list-text {
    display: flex;
    flex-direction: column;
    text-align: left;
}

.feature-list-text strong {
    font-size: 1.25rem;
    color: var(--text-white);
    margin-bottom: 6px;
    font-weight: 600;
}

.feature-list-text span {
    font-size: 1rem;
    color: var(--text-muted);
    line-height: 1.5;
}

@media (max-width: 900px) {
    .feature-grid {
        grid-template-columns: 1fr;
        gap: 50px;
    }
    
    .feature-content-col {
        align-items: center;
        text-align: center;
    }
    
    .feature-content-col h2.section-title {
        text-align: center !important;
    }

    .feature-list {
        gap: 32px;
    }

    .feature-list li {
        text-align: left; /* Mantém o texto justificado à esquerda para legibilidade */
    }
}"""

    # Replace the old Block 9 CSS (Lines matching .dif-container to end of .dif-bg-number etc)
    # the easiest way is a regex catch
    pattern = r'/\* Diferenciales Block \(Staggered Grid\) \*/.*?/\* Solution Section \*/'
    css_new = re.sub(pattern, new_css_block + '\n\n/* Solution Section */', css, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(css_new)


rewrite_html('index.html')
rewrite_css('style.css')

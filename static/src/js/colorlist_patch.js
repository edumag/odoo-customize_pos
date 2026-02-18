// Customize POS - Aplicar colores personalizados dinámicamente
(function() {
    'use strict';
    
    var colorsLoaded = false;
    
    function getColorsFromSession() {
        // Intentar obtener colores de múltiples fuentes
        var colors = null;
        
        // Fuente 1: odoo.session_info
        if (window.odoo && window.odoo.session_info) {
            if (window.odoo.session_info.customize_pos) {
                colors = window.odoo.session_info.customize_pos;
                console.log('[CustomizePOS] Colors found in odoo.session_info.customize_pos');
            }
        }
        
        return colors;
    }
    
    function fetchColorsFromServer() {
        // Hacer una petición al endpoint debug para obtener los colores
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/customize_pos/debug', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                try {
                    var response = JSON.parse(xhr.responseText);
                    console.log('[CustomizePOS] Colors fetched from server:', response);
                    
                    if (response.colors) {
                        var colors = {};
                        for (var i = 0; i < 12; i++) {
                            var key = 'color_' + i;
                            if (response.colors[key] && response.colors[key].value) {
                                colors['colorlist_' + i] = response.colors[key].value;
                            }
                        }
                        
                        if (Object.keys(colors).length > 0) {
                            injectColors(colors);
                            colorsLoaded = true;
                        }
                    }
                } catch (e) {
                    console.error('[CustomizePOS] Error parsing server response:', e);
                }
            }
        };
        
        xhr.send();
    }
    
    function injectColors(colors) {
        // Crear elemento style dinámico
        var styleId = 'customize-pos-dynamic-colors';
        var existingStyle = document.getElementById(styleId);
        if (existingStyle) {
            existingStyle.remove();
        }

        var style = document.createElement('style');
        style.id = styleId;
        style.type = 'text/css';

        // Generar CSS con las variables
        var cssContent = ':root {\n';
        for (var i = 0; i < 12; i++) {
            var color = colors['colorlist_' + i];
            if (color) {
                cssContent += '  --colorlist-color-' + i + ': ' + color + ';\n';
            }
        }
        cssContent += '}\n';

        style.innerHTML = cssContent;
        document.head.appendChild(style);

        console.log('[CustomizePOS] Colors injected successfully:', colors);
        colorsLoaded = true;
        return true;
    }
    
    function injectCustomColors() {
        if (colorsLoaded) {
            return true;
        }
        
        var colors = getColorsFromSession();
        
        if (colors) {
            return injectColors(colors);
        }
        
        console.log('[CustomizePOS] No colors in session, will fetch from server');
        return false;
    }

    var attempts = 0;
    var maxAttempts = 100;
    var serverFetchAttempted = false;
    
    function tryInject() {
        attempts++;
        
        if (injectCustomColors()) {
            console.log('[CustomizePOS] Successfully injected after', attempts, 'attempts');
            return;
        }
        
        // Si después de 50 intentos no hay colores en sesión, intentar fetch del servidor
        if (attempts > 50 && !serverFetchAttempted) {
            serverFetchAttempted = true;
            console.log('[CustomizePOS] Attempting to fetch colors from server...');
            fetchColorsFromServer();
        }
        
        if (attempts < maxAttempts) {
            setTimeout(tryInject, 100);
        } else {
            console.error('[CustomizePOS] Failed to inject colors after', maxAttempts, 'attempts');
            // Último intento: fetch del servidor
            if (!serverFetchAttempted) {
                fetchColorsFromServer();
            }
        }
    }

    function init() {
        console.log('[CustomizePOS] Initializing...');
        tryInject();
    }

    // Ejecutar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // También intentar cuando la página esté completamente cargada
    window.addEventListener('load', function() {
        console.log('[CustomizePOS] Window load event');
        if (!colorsLoaded) {
            injectCustomColors();
        }
    });

    // Re-inyectar periódicamente para el TPV
    setInterval(function() {
        if (!colorsLoaded && (document.querySelector('.pos') || document.querySelector('.o_colorlist'))) {
            injectCustomColors();
        }
    }, 2000);
})();

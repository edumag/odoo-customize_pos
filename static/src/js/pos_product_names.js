// Colorlist Customizer - Nombres de productos en mayúsculas
(function() {
    'use strict';
    
    console.log('[ColorlistCustomizer] Product names script loaded v2');
    
    // Variable para almacenar la configuración
    var config = {
        productNamesUppercase: false
    };
    
    function getSessionInfo() {
        // Intentar múltiples fuentes
        if (window.odoo && window.odoo.session_info) {
            return window.odoo.session_info;
        }
        if (window.sessionStorage) {
            var stored = window.sessionStorage.getItem('odoo_session_info');
            if (stored) {
                try {
                    return JSON.parse(stored);
                } catch(e) {}
            }
        }
        return null;
    }
    
    function loadConfig() {
        var session = getSessionInfo();
        if (session && session.colorlist_customizer_product_uppercase !== undefined) {
            config.productNamesUppercase = session.colorlist_customizer_product_uppercase;
            console.log('[ColorlistCustomizer] Config loaded from session:', config);
            return true;
        }
        return false;
    }
    
    function applyProductNamesStyle() {
        console.log('[ColorlistCustomizer] Applying style, config:', config);
        
        var body = document.body;
        if (!body) {
            console.log('[ColorlistCustomizer] No body found');
            return false;
        }
        
        if (config.productNamesUppercase === true) {
            body.classList.add('product-names-uppercase');
            console.log('[ColorlistCustomizer] Class ADDED');
        } else {
            body.classList.remove('product-names-uppercase');
            console.log('[ColorlistCustomizer] Class removed');
        }
        return true;
    }
    
    // Intentar cargar desde el backend mediante AJAX
    function fetchConfig() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/colorlist_customizer/config', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                try {
                    var data = JSON.parse(xhr.responseText);
                    config.productNamesUppercase = data.product_names_uppercase;
                    console.log('[ColorlistCustomizer] Config fetched:', data);
                    applyProductNamesStyle();
                } catch(e) {
                    console.log('[ColorlistCustomizer] Error parsing config:', e);
                }
            }
        };
        xhr.send();
    }
    
    // Función principal
    function init() {
        console.log('[ColorlistCustomizer] Init called');
        
        // Intentar cargar de la sesión
        if (loadConfig()) {
            applyProductNamesStyle();
        } else {
            // Si no está en sesión, intentar fetch
            console.log('[ColorlistCustomizer] Trying fetch...');
            fetchConfig();
        }
    }
    
    // Iniciar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Reintentar varias veces
    var attempts = 0;
    var retryInterval = setInterval(function() {
        attempts++;
        if (attempts > 10) {
            clearInterval(retryInterval);
            console.log('[ColorlistCustomizer] Stopped retrying');
            return;
        }
        
        if (loadConfig()) {
            applyProductNamesStyle();
            clearInterval(retryInterval);
        }
    }, 1000);
    
    // Exponer globalmente
    window.colorlistCustomizerApply = function() {
        loadConfig();
        applyProductNamesStyle();
    };
    
})();

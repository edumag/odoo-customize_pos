// Colorlist Customizer - Nombres de productos y categorías en mayúsculas
(function() {
    'use strict';
    
    console.log('[ColorlistCustomizer] Script loaded v3');
    
    // Variable para almacenar la configuración
    var config = {
        productNamesUppercase: false,
        categoryNamesUppercase: false
    };
    
    function applyStyles() {
        console.log('[ColorlistCustomizer] Applying styles:', config);
        
        var body = document.body;
        if (!body) {
            console.log('[ColorlistCustomizer] No body found');
            return false;
        }
        
        // Productos
        if (config.productNamesUppercase === true) {
            body.classList.add('product-names-uppercase');
            console.log('[ColorlistCustomizer] Product names: ADDED');
        } else {
            body.classList.remove('product-names-uppercase');
            console.log('[ColorlistCustomizer] Product names: removed');
        }
        
        // Categorías
        if (config.categoryNamesUppercase === true) {
            body.classList.add('category-names-uppercase');
            console.log('[ColorlistCustomizer] Category names: ADDED');
        } else {
            body.classList.remove('category-names-uppercase');
            console.log('[ColorlistCustomizer] Category names: removed');
        }
        
        return true;
    }
    
    function fetchConfig() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/colorlist_customizer/config', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                try {
                    var data = JSON.parse(xhr.responseText);
                    config.productNamesUppercase = data.product_names_uppercase;
                    config.categoryNamesUppercase = data.category_names_uppercase;
                    console.log('[ColorlistCustomizer] Config fetched:', data);
                    applyStyles();
                } catch(e) {
                    console.log('[ColorlistCustomizer] Error parsing config:', e);
                }
            }
        };
        xhr.send();
    }
    
    // Función principal
    function init() {
        console.log('[ColorlistCustomizer] Initializing...');
        fetchConfig();
    }
    
    // Iniciar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Reintentar después de un tiempo
    setTimeout(function() {
        if (!document.body || !document.body.classList.contains('product-names-uppercase')) {
            console.log('[ColorlistCustomizer] Retrying...');
            fetchConfig();
        }
    }, 3000);
    
    // Exponer globalmente
    window.colorlistCustomizerApply = function() {
        fetchConfig();
    };
    
})();

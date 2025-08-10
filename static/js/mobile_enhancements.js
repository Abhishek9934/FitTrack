// Mobile enhancements for Fitness Tracker PWA
(function() {
    'use strict';

    // PWA Installation
    let deferredPrompt;
    let installButton;

    // Create install button
    function createInstallButton() {
        const button = document.createElement('button');
        button.id = 'install-button';
        button.innerHTML = '📱 Install App';
        button.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: linear-gradient(135deg, #FF6B6B, #FF8E53);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 25px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            z-index: 1000;
            box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
            transition: all 0.3s ease;
            display: none;
        `;
        
        button.addEventListener('click', installApp);
        document.body.appendChild(button);
        return button;
    }

    // Install PWA
    async function installApp() {
        if (deferredPrompt) {
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            
            if (outcome === 'accepted') {
                console.log('PWA installed');
                installButton.style.display = 'none';
            }
            
            deferredPrompt = null;
        }
    }

    // PWA Events
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        
        if (!installButton) {
            installButton = createInstallButton();
        }
        installButton.style.display = 'block';
    });

    window.addEventListener('appinstalled', () => {
        console.log('PWA was installed');
        if (installButton) {
            installButton.style.display = 'none';
        }
    });

    // Touch enhancements
    function addTouchEnhancements() {
        // Add touch feedback to buttons
        const buttons = document.querySelectorAll('button');
        buttons.forEach(button => {
            button.addEventListener('touchstart', function() {
                this.style.transform = 'scale(0.95)';
            });
            
            button.addEventListener('touchend', function() {
                setTimeout(() => {
                    this.style.transform = 'scale(1)';
                }, 100);
            });
        });

        // Prevent zoom on input focus (iOS)
        const inputs = document.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                const viewport = document.querySelector('meta[name=viewport]');
                if (viewport) {
                    viewport.setAttribute('content', 
                        'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no');
                }
            });
            
            input.addEventListener('blur', function() {
                const viewport = document.querySelector('meta[name=viewport]');
                if (viewport) {
                    viewport.setAttribute('content', 
                        'width=device-width, initial-scale=1.0, user-scalable=yes');
                }
            });
        });
    }

    // Mobile navigation enhancements
    function enhanceMobileNavigation() {
        // Add swipe gestures for page navigation
        let startX, startY, distX, distY;
        
        document.addEventListener('touchstart', function(e) {
            const touch = e.touches[0];
            startX = touch.clientX;
            startY = touch.clientY;
        });
        
        document.addEventListener('touchmove', function(e) {
            if (!startX || !startY) return;
            
            const touch = e.touches[0];
            distX = touch.clientX - startX;
            distY = touch.clientY - startY;
        });
        
        document.addEventListener('touchend', function(e) {
            if (!startX || !startY) return;
            
            // Swipe threshold
            const threshold = 100;
            const restraint = 100;
            
            // Right swipe (back)
            if (distX >= threshold && Math.abs(distY) <= restraint) {
                // Trigger back navigation if possible
                if (window.history.length > 1) {
                    window.history.back();
                }
            }
            
            // Reset values
            startX = startY = distX = distY = null;
        });
    }

    // Optimize for mobile viewport
    function optimizeViewport() {
        // Create or update viewport meta tag
        let viewport = document.querySelector('meta[name=viewport]');
        if (!viewport) {
            viewport = document.createElement('meta');
            viewport.name = 'viewport';
            document.head.appendChild(viewport);
        }
        
        viewport.content = 'width=device-width, initial-scale=1.0, user-scalable=yes, ' +
                          'minimum-scale=1.0, maximum-scale=3.0, viewport-fit=cover';
        
        // Add mobile-specific meta tags
        const metaTags = [
            { name: 'mobile-web-app-capable', content: 'yes' },
            { name: 'apple-mobile-web-app-capable', content: 'yes' },
            { name: 'apple-mobile-web-app-status-bar-style', content: 'default' },
            { name: 'apple-mobile-web-app-title', content: 'Fitness Tracker' },
            { name: 'theme-color', content: '#FF6B6B' },
            { name: 'msapplication-TileColor', content: '#FF6B6B' }
        ];
        
        metaTags.forEach(tag => {
            let meta = document.querySelector(`meta[name="${tag.name}"]`);
            if (!meta) {
                meta = document.createElement('meta');
                meta.name = tag.name;
                meta.content = tag.content;
                document.head.appendChild(meta);
            }
        });
    }

    // Performance optimizations
    function optimizePerformance() {
        // Lazy load images
        const images = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
        
        // Debounce resize events
        let resizeTimeout;
        window.addEventListener('resize', function() {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(function() {
                // Trigger any resize-dependent updates
                window.dispatchEvent(new Event('optimizedResize'));
            }, 250);
        });
    }

    // Service Worker registration
    function registerServiceWorker() {
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/static/sw.js')
                .then(registration => {
                    console.log('Service Worker registered successfully');
                })
                .catch(error => {
                    console.log('Service Worker registration failed');
                });
        }
    }

    // Notification support
    function enableNotifications() {
        if ('Notification' in window && 'serviceWorker' in navigator) {
            // Request permission for notifications
            if (Notification.permission === 'default') {
                // You can add a button to request permissions when user wants it
                console.log('Notification permission not granted yet');
            }
        }
    }

    // Haptic feedback (if supported)
    function addHapticFeedback() {
        const buttons = document.querySelectorAll('button[type="submit"], .stButton button');
        buttons.forEach(button => {
            button.addEventListener('click', function() {
                if (navigator.vibrate) {
                    navigator.vibrate(50); // Short vibration
                }
            });
        });
    }

    // Initialize all enhancements
    function init() {
        optimizeViewport();
        addTouchEnhancements();
        enhanceMobileNavigation();
        optimizePerformance();
        registerServiceWorker();
        enableNotifications();
        addHapticFeedback();
        
        console.log('Mobile enhancements initialized');
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Re-run enhancements when Streamlit updates the page
    const observer = new MutationObserver(function(mutations) {
        let shouldUpdate = false;
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                shouldUpdate = true;
            }
        });
        
        if (shouldUpdate) {
            setTimeout(() => {
                addTouchEnhancements();
                addHapticFeedback();
            }, 100);
        }
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

})();
import streamlit as st

def render_mobile_navigation():
    """Render fixed mobile bottom navigation bar"""
    
    # Get current page to highlight active button
    import urllib.parse
    current_path = st.query_params.get("page", "")
    
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
    /* Fixed bottom navigation bar */
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-top: 1px solid rgba(0, 0, 0, 0.1);
        padding: 8px 0 max(8px, env(safe-area-inset-bottom));
        z-index: 1000;
        display: flex;
        justify-content: space-around;
        align-items: center;
        box-shadow: 0 -2px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Navigation items */
    .nav-btn {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 8px 12px;
        border-radius: 12px;
        text-decoration: none;
        color: #8e8e93;
        font-size: 10px;
        font-weight: 500;
        transition: all 0.2s ease;
        cursor: pointer;
        min-width: 60px;
        background: none;
        border: none;
    }
    
    .nav-btn:hover {
        background: rgba(0, 122, 255, 0.1);
        color: #007aff;
        transform: translateY(-1px);
    }
    
    .nav-btn.active {
        color: #007aff;
        background: rgba(0, 122, 255, 0.1);
    }
    
    .nav-btn.active::before {
        content: '';
        position: absolute;
        top: -1px;
        left: 50%;
        transform: translateX(-50%);
        width: 4px;
        height: 4px;
        background: #007aff;
        border-radius: 50%;
    }
    
    .nav-icon {
        font-size: 20px;
        margin-bottom: 2px;
        transition: transform 0.2s ease;
    }
    
    .nav-btn:hover .nav-icon {
        transform: scale(1.1);
    }
    
    .nav-label {
        font-size: 10px;
        font-weight: 500;
        line-height: 1;
    }
    
    /* Add safe area for iPhones */
    @supports (padding: max(0px)) {
        .bottom-nav {
            padding-bottom: max(8px, env(safe-area-inset-bottom));
        }
    }
    
    /* Add bottom padding to main content */
    .main > div {
        padding-bottom: 90px !important;
    }
    
    /* Hide Streamlit sidebar on mobile */
    @media (max-width: 768px) {
        .css-1d391kg {
            display: none !important;
        }
        
        .css-18e3th9 {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
    }
    
    /* Responsive adjustments */
    @media (max-width: 480px) {
        .nav-btn {
            min-width: 50px;
            padding: 6px 8px;
        }
        
        .nav-icon {
            font-size: 18px;
        }
        
        .nav-label {
            font-size: 9px;
        }
    }
    </style>
    
    <div class="bottom-nav">
        <button class="nav-btn" onclick="window.location.href='/'" id="nav-home">
            <i class="fas fa-home nav-icon"></i>
            <span class="nav-label">Home</span>
        </button>
        
        <button class="nav-btn" onclick="window.location.href='/1_Weekly_Entry'" id="nav-entry">
            <i class="fas fa-plus-circle nav-icon"></i>
            <span class="nav-label">Log</span>
        </button>
        
        <button class="nav-btn" onclick="window.location.href='/2_Progress_Analytics'" id="nav-analytics">
            <i class="fas fa-chart-line nav-icon"></i>
            <span class="nav-label">Stats</span>
        </button>
        
        <button class="nav-btn" onclick="window.location.href='/3_Plan_Overview'" id="nav-plan">
            <i class="fas fa-clipboard-list nav-icon"></i>
            <span class="nav-label">Plan</span>
        </button>
    </div>
    
    <script>
    // Set active navigation item based on current page
    function setActiveNav() {
        const currentPath = window.location.pathname;
        const navItems = document.querySelectorAll('.nav-btn');
        
        // Remove active class from all items
        navItems.forEach(item => item.classList.remove('active'));
        
        // Add active class to current page
        if (currentPath === '/' || currentPath === '' || currentPath.includes('app.py')) {
            document.getElementById('nav-home').classList.add('active');
        } else if (currentPath.includes('1_Weekly_Entry')) {
            document.getElementById('nav-entry').classList.add('active');
        } else if (currentPath.includes('2_Progress_Analytics')) {
            document.getElementById('nav-analytics').classList.add('active');
        } else if (currentPath.includes('3_Plan_Overview')) {
            document.getElementById('nav-plan').classList.add('active');
        }
    }
    
    // Run on page load
    document.addEventListener('DOMContentLoaded', setActiveNav);
    
    // Add haptic feedback for mobile devices
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            if (navigator.vibrate) {
                navigator.vibrate(50);
            }
        });
    });
    </script>
    """, unsafe_allow_html=True)

def add_mobile_header(page_title, icon_class="fas fa-mobile-alt"):
    """Add mobile-friendly header with modern design"""
    st.markdown(f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
    .mobile-header {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.25rem 1rem;
        margin: -1rem -1rem 1.5rem -1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }}
    
    .mobile-header::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><g fill="%23ffffff" fill-opacity="0.1"><circle cx="20" cy="20" r="4"/><circle cx="40" cy="40" r="4"/></g></svg>');
        opacity: 0.5;
    }}
    
    .header-content {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        position: relative;
        z-index: 1;
    }}
    
    .header-icon {{
        font-size: 1.5rem;
        color: #ffffff;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }}
    
    .header-title {{
        margin: 0;
        font-size: 1.25rem;
        font-weight: 600;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        letter-spacing: 0.5px;
    }}
    
    @media (max-width: 768px) {{
        .mobile-header {{
            padding: 1rem;
        }}
        
        .header-title {{
            font-size: 1.1rem;
        }}
        
        .header-icon {{
            font-size: 1.3rem;
        }}
    }}
    </style>
    
    <div class="mobile-header">
        <div class="header-content">
            <i class="{icon_class} header-icon"></i>
            <h1 class="header-title">{page_title}</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

def add_floating_action_button(text="💾 Save", color="#4ECDC4"):
    """Add floating action button for primary actions"""
    st.markdown(f"""
    <style>
    .fab {{
        position: fixed;
        bottom: 90px;
        right: 20px;
        background: {color};
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        cursor: pointer;
        z-index: 999;
        transition: all 0.3s ease;
    }}
    
    .fab:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }}
    
    .fab:active {{
        transform: translateY(0);
    }}
    </style>
    
    <button class="fab">{text}</button>
    """, unsafe_allow_html=True)
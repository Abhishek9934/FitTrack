import streamlit as st

def render_mobile_navigation():
    """Render mobile-friendly bottom navigation with Font Awesome icons"""
    # Get current page to highlight active nav item
    current_page = st.session_state.get('current_page', 'home')
    
    st.markdown("""
    <!-- Font Awesome CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
    /* Mobile Navigation Bar */
    .mobile-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%);
        border-top: 1px solid #e0e6ed;
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 0.75rem 0.5rem;
        z-index: 1000;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
    }
    
    .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-width: 50px;
        padding: 0.5rem 0.25rem;
        border-radius: 12px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
        text-decoration: none;
        color: #6b7280;
    }
    
    .nav-item:hover {
        background: rgba(239, 68, 68, 0.1);
        color: #ef4444;
        transform: translateY(-2px);
    }
    
    .nav-item.active {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        box-shadow: 0 4px 16px rgba(239, 68, 68, 0.3);
        transform: translateY(-2px);
    }
    
    .nav-item.active::before {
        content: '';
        position: absolute;
        top: -8px;
        left: 50%;
        transform: translateX(-50%);
        width: 4px;
        height: 4px;
        background: #ef4444;
        border-radius: 50%;
    }
    
    .nav-icon {
        font-size: 1.25rem;
        margin-bottom: 0.25rem;
        transition: transform 0.2s ease;
    }
    
    .nav-item:hover .nav-icon {
        transform: scale(1.1);
    }
    
    .nav-label {
        font-size: 0.7rem;
        font-weight: 500;
        text-align: center;
        line-height: 1;
    }
    
    /* Add bottom padding to main content */
    .main > div {
        padding-bottom: 90px !important;
    }
    
    /* Hide default Streamlit sidebar on mobile */
    @media (max-width: 768px) {
        .css-1d391kg {
            display: none !important;
        }
        
        .css-18e3th9 {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        
        /* Responsive nav adjustments */
        .nav-item {
            min-width: 45px;
            padding: 0.4rem 0.2rem;
        }
        
        .nav-icon {
            font-size: 1.1rem;
        }
        
        .nav-label {
            font-size: 0.65rem;
        }
    }
    
    /* Add subtle animations */
    @keyframes navPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .nav-item.active .nav-icon {
        animation: navPulse 2s ease-in-out infinite;
    }
    </style>
    
    <nav class="mobile-nav">
        <div class="nav-item" onclick="navigateToPage('/')" id="nav-home">
            <i class="fas fa-home nav-icon"></i>
            <span class="nav-label">Home</span>
        </div>
        <div class="nav-item" onclick="navigateToPage('/1_Weekly_Entry')" id="nav-entry">
            <i class="fas fa-plus-circle nav-icon"></i>
            <span class="nav-label">Log</span>
        </div>
        <div class="nav-item" onclick="navigateToPage('/2_Progress_Analytics')" id="nav-analytics">
            <i class="fas fa-chart-line nav-icon"></i>
            <span class="nav-label">Stats</span>
        </div>
        <div class="nav-item" onclick="navigateToPage('/3_Plan_Overview')" id="nav-plan">
            <i class="fas fa-clipboard-list nav-icon"></i>
            <span class="nav-label">Plan</span>
        </div>
    </nav>
    
    <script>
    function navigateToPage(page) {
        // Add haptic feedback for iOS
        if (navigator.vibrate) {
            navigator.vibrate(50);
        }
        
        // Remove active class from all nav items
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
        });
        
        // Add active class to clicked item
        if (page === '/') {
            document.getElementById('nav-home').classList.add('active');
        } else if (page === '/1_Weekly_Entry') {
            document.getElementById('nav-entry').classList.add('active');
        } else if (page === '/2_Progress_Analytics') {
            document.getElementById('nav-analytics').classList.add('active');
        } else if (page === '/3_Plan_Overview') {
            document.getElementById('nav-plan').classList.add('active');
        }
        
        // Navigate to page
        setTimeout(() => {
            window.location.href = page;
        }, 150);
    }
    
    // Set active nav item based on current page
    document.addEventListener('DOMContentLoaded', function() {
        const currentPath = window.location.pathname;
        
        // Remove active from all first
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
        });
        
        // Set active based on current path
        if (currentPath === '/' || currentPath === '') {
            document.getElementById('nav-home').classList.add('active');
        } else if (currentPath.includes('1_Weekly_Entry')) {
            document.getElementById('nav-entry').classList.add('active');
        } else if (currentPath.includes('2_Progress_Analytics')) {
            document.getElementById('nav-analytics').classList.add('active');
        } else if (currentPath.includes('3_Plan_Overview')) {
            document.getElementById('nav-plan').classList.add('active');
        }
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
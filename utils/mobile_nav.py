import streamlit as st

def render_mobile_navigation():
    """Render fixed mobile bottom navigation"""
    
    # Add padding to main content and create the fixed navigation
    st.markdown("""
    <style>
    /* Add bottom padding to main content for navigation space */
    .main > div {
        padding-bottom: 100px !important;
    }
    
    /* Hide Streamlit sidebar on mobile */
    @media (max-width: 768px) {
        [data-testid="stSidebar"] {
            display: none !important;
        }
    }
    
    /* Fixed navigation container */
    .fixed-nav-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: white;
        border-top: 2px solid #e0e6ed;
        padding: 12px 8px;
        z-index: 999999;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
        backdrop-filter: blur(10px);
    }
    
    /* Navigation grid layout */
    .nav-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 8px;
        max-width: 500px;
        margin: 0 auto;
    }
    
    /* Navigation buttons */
    .nav-button {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 12px 8px;
        text-align: center;
        text-decoration: none;
        color: #495057;
        font-size: 12px;
        font-weight: 500;
        transition: all 0.2s ease;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
    }
    
    .nav-button:hover {
        background: #e9ecef;
        color: #007bff;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(0,123,255,0.2);
    }
    
    .nav-button-icon {
        font-size: 20px;
        line-height: 1;
    }
    
    .nav-button-label {
        font-size: 11px;
        font-weight: 500;
        line-height: 1;
    }
    
    /* Mobile responsive */
    @media (max-width: 480px) {
        .nav-button {
            padding: 10px 6px;
        }
        
        .nav-button-icon {
            font-size: 18px;
        }
        
        .nav-button-label {
            font-size: 10px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create the fixed navigation HTML
    st.markdown("""
    <div class="fixed-nav-container">
        <div class="nav-grid">
            <a href="/" class="nav-button">
                <div class="nav-button-icon">🏠</div>
                <div class="nav-button-label">Home</div>
            </a>
            <a href="/1_Weekly_Entry" class="nav-button">
                <div class="nav-button-icon">📝</div>
                <div class="nav-button-label">Log</div>
            </a>
            <a href="/2_Progress_Analytics" class="nav-button">
                <div class="nav-button-icon">📊</div>
                <div class="nav-button-label">Stats</div>
            </a>
            <a href="/3_Plan_Overview" class="nav-button">
                <div class="nav-button-icon">📋</div>
                <div class="nav-button-label">Plan</div>
            </a>
        </div>
    </div>
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
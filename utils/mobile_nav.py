import streamlit as st

def render_mobile_navigation():
    """Render fixed mobile bottom navigation with working buttons"""
    
    # Add the fixed navigation styling and positioning
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
    .mobile-nav-fixed {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: white;
        border-top: 2px solid #e0e6ed;
        padding: 8px;
        z-index: 999999;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
    }
    
    /* Make navigation buttons full width and mobile-friendly */
    .mobile-nav-fixed .stButton > button {
        width: 100%;
        height: 60px;
        border-radius: 12px;
        border: 1px solid #dee2e6;
        background: #f8f9fa;
        color: #495057;
        font-size: 11px;
        font-weight: 500;
        transition: all 0.2s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 2px;
        padding: 8px 4px;
    }
    
    .mobile-nav-fixed .stButton > button:hover {
        background: #e9ecef;
        color: #007bff;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(0,123,255,0.2);
    }
    
    /* Mobile responsive adjustments */
    @media (max-width: 480px) {
        .mobile-nav-fixed .stButton > button {
            height: 55px;
            font-size: 10px;
        }
        
        .mobile-nav-fixed {
            padding: 6px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create a container with fixed positioning
    st.markdown('<div class="mobile-nav-fixed">', unsafe_allow_html=True)
    
    # Create the navigation buttons using Streamlit columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏠\nHome", key="fixed_nav_home", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("📝\nLog", key="fixed_nav_log", use_container_width=True):
            st.switch_page("pages/1_Weekly_Entry.py")
    
    with col3:
        if st.button("📊\nStats", key="fixed_nav_stats", use_container_width=True):
            st.switch_page("pages/2_Progress_Analytics.py")
    
    with col4:
        if st.button("📋\nPlan", key="fixed_nav_plan", use_container_width=True):
            st.switch_page("pages/3_Plan_Overview.py")
    
    st.markdown('</div>', unsafe_allow_html=True)

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
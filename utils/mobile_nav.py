import streamlit as st

def render_mobile_navigation():
    """Render fixed mobile bottom navigation using components"""
    
    # Add CSS styles first
    st.markdown("""
    <style>
    /* Add bottom padding to main content for navigation space */
    .main > div {
        padding-bottom: 90px !important;
    }
    
    /* Hide Streamlit sidebar on mobile */
    @media (max-width: 768px) {
        [data-testid="stSidebar"] {
            display: none !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create a fixed container at the bottom
    nav_container = st.container()
    
    with nav_container:
        # Add the navigation HTML in a separate markdown block
        st.markdown("""
        <div style="
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            border-top: 1px solid #ddd;
            padding: 10px 0;
            z-index: 999;
            display: flex;
            justify-content: space-around;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        ">
        </div>
        """, unsafe_allow_html=True)
    
    # Create navigation using Streamlit columns instead
    st.markdown("---")
    st.subheader("Quick Navigation")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏠\nHome", key="nav_home_btn", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("📝\nLog", key="nav_log_btn", use_container_width=True):
            st.switch_page("pages/1_Weekly_Entry.py")
    
    with col3:
        if st.button("📊\nStats", key="nav_stats_btn", use_container_width=True):
            st.switch_page("pages/2_Progress_Analytics.py")
    
    with col4:
        if st.button("📋\nPlan", key="nav_plan_btn", use_container_width=True):
            st.switch_page("pages/3_Plan_Overview.py")

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
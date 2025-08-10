import streamlit as st

def render_mobile_navigation():
    """Render mobile-friendly bottom navigation"""
    st.markdown("""
    <style>
    .mobile-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: white;
        border-top: 1px solid #E0E0E0;
        display: flex;
        justify-content: space-around;
        padding: 0.75rem 0;
        z-index: 1000;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    }
    
    .mobile-nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none;
        color: #666;
        font-size: 0.8rem;
        min-width: 60px;
        padding: 0.5rem 0.25rem;
        border-radius: 8px;
        transition: all 0.2s ease;
    }
    
    .mobile-nav-item:hover {
        background: #F8F9FA;
        color: #FF6B6B;
        transform: translateY(-1px);
    }
    
    .mobile-nav-item.active {
        background: #FF6B6B;
        color: white;
        font-weight: 600;
    }
    
    .mobile-nav-icon {
        font-size: 1.2rem;
        margin-bottom: 0.25rem;
    }
    
    /* Add bottom padding to main content to prevent overlap */
    .main > div {
        padding-bottom: 100px !important;
    }
    
    /* Hide sidebar on mobile for cleaner experience */
    @media (max-width: 768px) {
        .css-1d391kg {
            display: none;
        }
        
        /* Adjust main content for hidden sidebar */
        .css-18e3th9 {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
    }
    </style>
    
    <div class="mobile-nav">
        <div class="mobile-nav-item" data-page="/">
            <div class="mobile-nav-icon">🏠</div>
            <div>Dashboard</div>
        </div>
        <div class="mobile-nav-item" data-page="/1_Weekly_Entry">
            <div class="mobile-nav-icon">📝</div>
            <div>Log Entry</div>
        </div>
        <div class="mobile-nav-item" data-page="/2_Progress_Analytics">
            <div class="mobile-nav-icon">📊</div>
            <div>Analytics</div>
        </div>
        <div class="mobile-nav-item" data-page="/3_Plan_Overview">
            <div class="mobile-nav-icon">📋</div>
            <div>Plan</div>
        </div>
    </div>
    
    <script>
    // Add click handlers for navigation
    document.addEventListener('DOMContentLoaded', function() {
        const navItems = document.querySelectorAll('.mobile-nav-item[data-page]');
        navItems.forEach(item => {
            item.addEventListener('click', function() {
                const page = this.getAttribute('data-page');
                if (page === '/') {
                    window.location.href = '/';
                } else {
                    window.location.href = page;
                }
            });
        });
    });
    </script>
    """, unsafe_allow_html=True)

def add_mobile_header(page_title, icon="📱"):
    """Add mobile-friendly header with back navigation"""
    st.markdown(f"""
    <style>
    .mobile-header {{
        background: linear-gradient(135deg, #4ECDC4, #44A08D);
        color: white;
        padding: 1rem;
        margin: -1rem -1rem 1.5rem -1rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-radius: 0 0 16px 16px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.15);
    }}
    
    .mobile-header h1 {{
        margin: 0;
        font-size: 1.25rem;
        font-weight: 600;
    }}
    
    .back-btn {{
        background: rgba(255,255,255,0.2);
        border: none;
        color: white;
        padding: 0.5rem;
        border-radius: 50%;
        cursor: pointer;
        font-size: 1.1rem;
        transition: all 0.2s ease;
    }}
    
    .back-btn:hover {{
        background: rgba(255,255,255,0.3);
        transform: scale(1.05);
    }}
    </style>
    
    <div class="mobile-header">
        <button class="back-btn" onclick="window.history.back()">←</button>
        <h1>{icon} {page_title}</h1>
        <div style="width: 2.5rem;"></div>
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
import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling for cinematic UI"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 60px 20px;
        background: linear-gradient(135deg, rgba(15,12,41,0.9) 0%, rgba(48,43,99,0.9) 100%);
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        animation: fadeIn 1s ease-in;
    }
    
    .hero-title {
        font-family: 'Cinzel', serif;
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        color: #b8b8d1;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    
    /* Feature Cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 40px 0;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 15px;
    }
    
    .feature-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 10px;
    }
    
    .feature-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        color: #b8b8d1;
        line-height: 1.5;
    }
    
    /* Form Container */
    .form-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        margin: 30px 0;
        animation: slideUp 0.6s ease-out;
    }
    
    .section-title {
        font-family: 'Cinzel', serif;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Output Container */
    .output-container {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        animation: fadeIn 0.8s ease-in;
    }
    
    /* Character Cards */
    .character-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    
    .character-card:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .character-card h3 {
        color: #667eea;
        margin-bottom: 15px;
        font-family: 'Cinzel', serif;
    }
    
    .character-card p {
        color: #d1d1e0;
        line-height: 1.6;
        margin: 10px 0;
    }
    
    /* Sound Card */
    .sound-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #667eea;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    
    .sound-card:hover {
        background: rgba(102, 126, 234, 0.1);
        transform: translateX(5px);
    }
    
    .sound-card h4 {
        color: #667eea;
        margin-bottom: 10px;
    }
    
    .sound-card p {
        color: #d1d1e0;
        margin: 8px 0;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px 40px;
        font-size: 1.1rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.6);
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: #b8b8d1;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        padding: 12px 24px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Metrics */
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 15px;
    }
    
    /* Section Divider */
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 50px 0;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes glow {
        from {
            text-shadow: 0 0 10px rgba(102, 126, 234, 0.5);
        }
        to {
            text-shadow: 0 0 20px rgba(102, 126, 234, 0.8), 0 0 30px rgba(118, 75, 162, 0.6);
        }
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    </style>
    """, unsafe_allow_html=True)

def render_hero_section():
    """Render hero section with title and subtitle"""
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🎬 Scriptoria</div>
        <div class="hero-subtitle">
            AI-Powered Film Pre-Production Studio<br>
            Transform your story ideas into professional screenplays, cinematic storyboards, and production plans using AI.
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_feature_cards():
    """Render feature highlight cards"""
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📜</div>
            <div class="feature-title">Screenplay Generation</div>
            <div class="feature-desc">Professional formatted scripts with dialogue and scene descriptions</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎭</div>
            <div class="feature-title">Character Profiles</div>
            <div class="feature-desc">Detailed character backgrounds, motivations, and emotional arcs</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎬</div>
            <div class="feature-title">AI Storyboards</div>
            <div class="feature-desc">Visual scene representations with camera and lighting suggestions</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎧</div>
            <div class="feature-title">Sound Design</div>
            <div class="feature-desc">Music, ambient sounds, and emotional audio cues for each scene</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💰</div>
            <div class="feature-title">Budget Estimation</div>
            <div class="feature-desc">Comprehensive production cost breakdown and planning</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

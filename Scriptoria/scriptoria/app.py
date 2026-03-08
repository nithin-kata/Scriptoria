import streamlit as st
import os
from dotenv import load_dotenv
from utils.ai_generator import AIGenerator
from utils.ui_components import apply_custom_css, render_hero_section, render_feature_cards
from utils.exporter import export_screenplay, export_full_project

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Scriptoria - AI Film Studio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom styling
apply_custom_css()

# Initialize session state
if 'generated' not in st.session_state:
    st.session_state.generated = False
if 'project_data' not in st.session_state:
    st.session_state.project_data = {}

def main():
    # Hero Section
    render_hero_section()
    
    # Feature Cards
    render_feature_cards()
    
    # Main Content
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Story Input Form
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-title">🎬 Create Your Film Project</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            story_title = st.text_input(
                "Story Title",
                placeholder="Enter your film title...",
                key="story_title"
            )
            
            story_concept = st.text_area(
                "Story Concept",
                placeholder="Describe your story idea in detail...",
                height=200,
                key="story_concept"
            )
        
        with col2:
            genre = st.selectbox(
                "Genre",
                ["Action", "Drama", "Thriller", "Sci-Fi", "Romance", "Fantasy", "Horror", "Comedy"],
                key="genre"
            )
            
            num_characters = st.slider(
                "Number of Characters",
                min_value=1,
                max_value=10,
                value=3,
                key="num_characters"
            )
            
            film_duration = st.radio(
                "Film Duration",
                ["Short Film (< 40 min)", "Feature Film (90+ min)"],
                key="film_duration"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Generate Button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            generate_btn = st.button(
                "🎥 Generate Film Package",
                use_container_width=True,
                type="primary"
            )
    
    # AI Processing and Results
    if generate_btn:
        if not story_title or not story_concept:
            st.error("⚠️ Please provide both a story title and concept.")
            return
        
        api_key = os.getenv("HF_API_KEY")
        if not api_key:
            st.error("⚠️ Hugging Face API key not found. Please set HF_API_KEY in your .env file.")
            return
        
        # Initialize AI Generator
        ai_gen = AIGenerator(api_key)
        
        # Processing Animation
        with st.spinner("🎬 Creating your film pre-production package..."):
            try:
                # Generate all components
                screenplay = ai_gen.generate_screenplay(
                    story_title, story_concept, genre, film_duration
                )
                
                characters = ai_gen.generate_characters(
                    story_concept, genre, num_characters
                )
                
                sound_design = ai_gen.generate_sound_design(
                    story_concept, genre
                )
                
                budget = ai_gen.generate_budget(
                    film_duration, num_characters
                )
                
                storyboard_images = ai_gen.generate_storyboard_images(
                    story_concept, genre
                )
                
                # Store in session state
                st.session_state.project_data = {
                    'title': story_title,
                    'genre': genre,
                    'screenplay': screenplay,
                    'characters': characters,
                    'sound_design': sound_design,
                    'budget': budget,
                    'storyboard': storyboard_images
                }
                st.session_state.generated = True
                
            except Exception as e:
                st.error(f"❌ Error generating content: {str(e)}")
                return
    
    # Display Results Dashboard
    if st.session_state.generated:
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown('<h2 class="section-title">📋 Your Film Pre-Production Package</h2>', unsafe_allow_html=True)
        
        # Tabs for different outputs
        tabs = st.tabs(["📜 Screenplay", "🎭 Characters", "🎬 Storyboard", "🎧 Sound Design", "💰 Budget"])
        
        # Screenplay Tab
        with tabs[0]:
            st.markdown('<div class="output-container">', unsafe_allow_html=True)
            st.markdown(f"### {st.session_state.project_data['title']}")
            st.markdown(f"**Genre:** {st.session_state.project_data['genre']}")
            st.markdown("---")
            st.markdown(st.session_state.project_data['screenplay'])
            
            screenplay_txt = export_screenplay(st.session_state.project_data)
            st.download_button(
                "📥 Download Screenplay (TXT)",
                screenplay_txt,
                file_name=f"{st.session_state.project_data['title']}_screenplay.txt",
                mime="text/plain"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Characters Tab
        with tabs[1]:
            st.markdown('<div class="output-container">', unsafe_allow_html=True)
            characters = st.session_state.project_data['characters']
            
            cols = st.columns(min(len(characters), 3))
            for idx, char in enumerate(characters):
                with cols[idx % 3]:
                    st.markdown(f"""
                    <div class="character-card">
                        <h3>🎭 {char['name']}</h3>
                        <p><strong>Background:</strong> {char['background']}</p>
                        <p><strong>Personality:</strong> {char['personality']}</p>
                        <p><strong>Motivation:</strong> {char['motivation']}</p>
                        <p><strong>Arc:</strong> {char['arc']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Storyboard Tab
        with tabs[2]:
            st.markdown('<div class="output-container">', unsafe_allow_html=True)
            storyboard = st.session_state.project_data['storyboard']
            
            for scene in storyboard:
                st.markdown(f"### {scene['title']}")
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    if scene['image']:
                        st.image(scene['image'], use_container_width=True)
                    else:
                        st.info("Image generation in progress...")
                
                with col2:
                    st.markdown(f"**📷 Camera:** {scene['camera']}")
                    st.markdown(f"**💡 Lighting:** {scene['lighting']}")
                
                st.markdown("---")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Sound Design Tab
        with tabs[3]:
            st.markdown('<div class="output-container">', unsafe_allow_html=True)
            sound = st.session_state.project_data['sound_design']
            
            for scene_sound in sound:
                st.markdown(f"""
                <div class="sound-card">
                    <h4>🎧 {scene_sound['scene']}</h4>
                    <p><strong>Music:</strong> {scene_sound['music']}</p>
                    <p><strong>Ambient:</strong> {scene_sound['ambient']}</p>
                    <p><strong>Emotional Cue:</strong> {scene_sound['emotional']}</p>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Budget Tab
        with tabs[4]:
            st.markdown('<div class="output-container">', unsafe_allow_html=True)
            budget = st.session_state.project_data['budget']
            
            st.markdown("### 💰 Production Budget Breakdown")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cast", f"${budget['cast']:,}")
                st.metric("Equipment", f"${budget['equipment']:,}")
            with col2:
                st.metric("Crew", f"${budget['crew']:,}")
                st.metric("Sound", f"${budget['sound']:,}")
            with col3:
                st.metric("Locations", f"${budget['locations']:,}")
                st.metric("Post-Production", f"${budget['post_production']:,}")
            
            st.markdown("---")
            st.markdown(f"### Total Estimated Budget: ${budget['total']:,}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Export Options
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            screenplay_txt = export_screenplay(st.session_state.project_data)
            st.download_button(
                "📥 Download Screenplay (TXT)",
                screenplay_txt,
                file_name=f"{st.session_state.project_data['title']}_screenplay.txt",
                mime="text/plain"
            )
        
        with col2:
            pdf_bytes = export_full_project(st.session_state.project_data, format='pdf')
            st.download_button(
                "📥 Download Full Project (PDF)",
                pdf_bytes,
                file_name=f"{st.session_state.project_data['title']}_project.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()

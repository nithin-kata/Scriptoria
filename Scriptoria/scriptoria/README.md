# 🎬 Scriptoria - AI-Powered Film Pre-Production Studio

Transform your story ideas into professional screenplays, cinematic storyboards, and complete production plans using cutting-edge AI technology.

## ✨ Features

- **📜 Screenplay Generation** - Professional formatted scripts with dialogue, scene descriptions, and proper formatting
- **🎭 Character Profiles** - Detailed character backgrounds, personalities, motivations, and emotional arcs
- **🎬 AI Storyboards** - Visual scene representations with camera angles and lighting suggestions
- **🎧 Sound Design** - Music styles, ambient sounds, and emotional audio cues for each scene
- **💰 Budget Estimation** - Comprehensive production cost breakdown and financial planning

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Hugging Face API key ([Get one here](https://huggingface.co/settings/tokens))

### Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```

4. Edit `.env` and add your Hugging Face API key:
```
HF_API_KEY=your_actual_api_key_here
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 🎯 How to Use

1. **Enter Your Story Details**
   - Provide a compelling story title
   - Select your film genre
   - Describe your story concept in detail
   - Choose number of characters
   - Select film duration (Short or Feature)

2. **Generate Your Film Package**
   - Click "Generate Film Package"
   - Wait for AI to process (typically 30-60 seconds)

3. **Explore Your Results**
   - Navigate through tabs to view:
     - Complete screenplay
     - Character profiles
     - Storyboard images
     - Sound design suggestions
     - Budget breakdown

4. **Export Your Work**
   - Download screenplay as TXT
   - Export full project as PDF

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS
- **Backend**: Python
- **AI Models**:
  - Text Generation: `mistralai/Mistral-7B-Instruct-v0.1`
  - Image Generation: `stabilityai/stable-diffusion-xl-base-1.0`
- **API**: Hugging Face Inference API

## 📁 Project Structure

```
scriptoria/
├── app.py                      # Main Streamlit application
├── utils/
│   ├── ai_generator.py        # AI model integration
│   ├── prompts.py             # Prompt templates
│   ├── ui_components.py       # Custom UI components
│   └── exporter.py            # Export functionality
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # Documentation
```

## 🎨 UI Features

- Cinematic gradient backgrounds
- Smooth animations and transitions
- Responsive card layouts
- Professional typography
- Interactive hover effects
- Loading animations
- Modern glassmorphism design

## 🔧 Configuration

### API Rate Limits

The Hugging Face Inference API has rate limits. If you encounter 503 errors, the models are loading. The application automatically retries with delays.

### Customization

You can customize:
- AI model parameters in `utils/ai_generator.py`
- Prompt templates in `utils/prompts.py`
- UI styling in `utils/ui_components.py`
- Budget calculations in `ai_generator.py`

## 📝 Example Use Case

**Story Title**: "The Last Signal"

**Genre**: Sci-Fi

**Concept**: "In a post-apocalyptic world, a lone radio operator receives a mysterious signal from space that could save humanity or doom it forever."

The system will generate:
- A professional screenplay with properly formatted scenes
- 3 detailed character profiles with backgrounds and arcs
- AI-generated storyboard images for key scenes
- Sound design suggestions for atmospheric scenes
- Complete production budget estimate

## 🚀 Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add `HF_API_KEY` to secrets
4. Deploy

### Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Upload your files
3. Add `HF_API_KEY` to Space secrets
4. Your app will be live

### Local Production

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## ⚠️ Important Notes

- First API calls may take 20-30 seconds as models load
- Image generation requires significant processing time
- Keep your API key secure and never commit it to version control
- Free tier API has rate limits - consider upgrading for production use

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available for educational and commercial use.

## 🙏 Acknowledgments

- Hugging Face for providing AI model APIs
- Streamlit for the amazing web framework
- The open-source AI community

## 📧 Support

For issues or questions:
- Check the [Hugging Face documentation](https://huggingface.co/docs)
- Review [Streamlit documentation](https://docs.streamlit.io)
- Open an issue in the repository

---

**Built with ❤️ for filmmakers and storytellers**

🎬 Start creating your cinematic masterpiece today!

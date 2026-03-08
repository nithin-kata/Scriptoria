# 🏗️ Scriptoria - Architecture Documentation

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     SCRIPTORIA SYSTEM                        │
│                  AI Film Pre-Production Studio               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                      │
├─────────────────────────────────────────────────────────────┤
│  Streamlit Web Interface (app.py)                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Hero Section │  │ Input Forms  │  │ Results Tabs │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │Feature Cards │  │  Animations  │  │Export Buttons│     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      UI COMPONENTS LAYER                     │
├─────────────────────────────────────────────────────────────┤
│  ui_components.py                                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ • apply_custom_css()      - Cinematic styling        │  │
│  │ • render_hero_section()   - Hero display             │  │
│  │ • render_feature_cards()  - Feature highlights       │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                     BUSINESS LOGIC LAYER                     │
├─────────────────────────────────────────────────────────────┤
│  ai_generator.py (AIGenerator Class)                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ • generate_screenplay()    - Script generation       │  │
│  │ • generate_characters()    - Character profiles      │  │
│  │ • generate_sound_design()  - Audio suggestions       │  │
│  │ • generate_budget()        - Cost estimation         │  │
│  │ • generate_storyboard_images() - Visual scenes       │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      PROMPT ENGINEERING                      │
├─────────────────────────────────────────────────────────────┤
│  prompts.py                                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ • create_screenplay_prompt()   - Script prompts      │  │
│  │ • create_character_prompt()    - Character prompts   │  │
│  │ • create_sound_design_prompt() - Sound prompts       │  │
│  │ • create_storyboard_prompt()   - Image prompts       │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      EXTERNAL AI LAYER                       │
├─────────────────────────────────────────────────────────────┤
│  Hugging Face Inference API                                 │
│  ┌────────────────────┐      ┌────────────────────┐        │
│  │  Mistral-7B        │      │ Stable Diffusion   │        │
│  │  Text Generation   │      │ Image Generation   │        │
│  └────────────────────┘      └────────────────────┘        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      EXPORT LAYER                            │
├─────────────────────────────────────────────────────────────┤
│  exporter.py                                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ • export_screenplay()    - TXT export                │  │
│  │ • export_full_project()  - PDF export                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

```
USER INPUT
    │
    ├─ Story Title
    ├─ Genre Selection
    ├─ Story Concept
    ├─ Number of Characters
    └─ Film Duration
    │
    ↓
VALIDATION
    │
    ├─ Check required fields
    ├─ Verify API key
    └─ Validate inputs
    │
    ↓
AI GENERATION (Parallel Processing)
    │
    ├─────────────────┬─────────────────┬─────────────────┐
    ↓                 ↓                 ↓                 ↓
SCREENPLAY      CHARACTERS      SOUND DESIGN      STORYBOARD
    │                 │                 │                 │
    │                 │                 │                 │
Mistral-7B      Mistral-7B      Mistral-7B      SD-XL
Text API        Text API        Text API        Image API
    │                 │                 │                 │
    └─────────────────┴─────────────────┴─────────────────┘
                            │
                            ↓
                    BUDGET CALCULATION
                            │
                            ↓
                    SESSION STATE STORAGE
                            │
                            ↓
                    RESULTS DISPLAY
                            │
    ┌───────────────────────┼───────────────────────┐
    │                       │                       │
SCREENPLAY TAB      CHARACTERS TAB      STORYBOARD TAB
    │                       │                       │
SOUND TAB           BUDGET TAB          EXPORT OPTIONS
```

---

## Component Architecture

### 1. Main Application (app.py)

```python
app.py
├── Configuration
│   ├── Page config
│   ├── Session state
│   └── Environment loading
│
├── UI Rendering
│   ├── Hero section
│   ├── Feature cards
│   └── Input forms
│
├── Event Handling
│   ├── Generate button
│   ├── Form validation
│   └── Error handling
│
├── AI Processing
│   ├── Initialize AIGenerator
│   ├── Call generation methods
│   └── Store results
│
└── Results Display
    ├── Tabbed interface
    ├── Content rendering
    └── Export options
```

### 2. AI Generator (ai_generator.py)

```python
AIGenerator Class
├── __init__(api_key)
│   ├── Store API key
│   ├── Set model names
│   └── Configure headers
│
├── _call_text_api(prompt)
│   ├── Build request
│   ├── Handle retries
│   ├── Parse response
│   └── Return text
│
├── _call_image_api(prompt)
│   ├── Build request
│   ├── Handle retries
│   ├── Parse image
│   └── Return PIL Image
│
├── generate_screenplay()
│   ├── Create prompt
│   ├── Call text API
│   └── Return screenplay
│
├── generate_characters()
│   ├── Loop for each character
│   ├── Create prompts
│   ├── Call text API
│   ├── Parse results
│   └── Return character list
│
├── generate_sound_design()
│   ├── Create prompt
│   ├── Call text API
│   ├── Parse scenes
│   └── Return sound list
│
├── generate_budget()
│   ├── Calculate costs
│   ├── Apply multipliers
│   └── Return budget dict
│
└── generate_storyboard_images()
    ├── Define scenes
    ├── Create prompts
    ├── Call image API
    └── Return storyboard list
```

### 3. UI Components (ui_components.py)

```python
ui_components.py
├── apply_custom_css()
│   ├── Global styles
│   ├── Component styles
│   ├── Animations
│   └── Responsive design
│
├── render_hero_section()
│   ├── Title with gradient
│   ├── Subtitle
│   └── Container styling
│
└── render_feature_cards()
    ├── Grid layout
    ├── Card components
    ├── Icons and text
    └── Hover effects
```

### 4. Prompts (prompts.py)

```python
prompts.py
├── create_screenplay_prompt()
│   ├── Format instructions
│   ├── Genre adaptation
│   └── Duration scaling
│
├── create_character_prompt()
│   ├── Character structure
│   ├── Detail requirements
│   └── Context integration
│
├── create_sound_design_prompt()
│   ├── Scene breakdown
│   ├── Audio categories
│   └── Genre styling
│
└── create_storyboard_prompt()
    ├── Visual keywords
    ├── Cinematic terms
    └── Quality modifiers
```

### 5. Exporter (exporter.py)

```python
exporter.py
├── export_screenplay(data)
│   ├── Format text
│   ├── Add headers
│   └── Return string
│
└── export_full_project(data)
    ├── Create PDF
    ├── Add sections
    │   ├── Title page
    │   ├── Screenplay
    │   ├── Characters
    │   ├── Sound design
    │   └── Budget
    └── Return bytes
```

---

## State Management

```
Session State Structure
├── generated (bool)
│   └── Tracks if content has been generated
│
└── project_data (dict)
    ├── title (str)
    ├── genre (str)
    ├── screenplay (str)
    ├── characters (list)
    │   └── [{name, background, personality, motivation, arc}]
    ├── sound_design (list)
    │   └── [{scene, music, ambient, emotional}]
    ├── budget (dict)
    │   └── {cast, crew, equipment, locations, sound, post_production, total}
    └── storyboard (list)
        └── [{title, image, camera, lighting}]
```

---

## API Integration Flow

```
API Call Sequence
│
├─ 1. User clicks "Generate"
│   └─ Validate inputs
│
├─ 2. Initialize AIGenerator
│   └─ Load API key from environment
│
├─ 3. Generate Screenplay
│   ├─ Create prompt
│   ├─ POST to Mistral-7B API
│   ├─ Wait for response (10-20s)
│   └─ Parse and store
│
├─ 4. Generate Characters (Loop)
│   ├─ For each character:
│   │   ├─ Create prompt
│   │   ├─ POST to Mistral-7B API
│   │   ├─ Wait for response (5-10s)
│   │   └─ Parse and store
│   └─ Combine results
│
├─ 5. Generate Sound Design
│   ├─ Create prompt
│   ├─ POST to Mistral-7B API
│   ├─ Wait for response (8-15s)
│   └─ Parse and store
│
├─ 6. Calculate Budget
│   └─ Local calculation (<1s)
│
├─ 7. Generate Storyboard (Loop)
│   ├─ For each scene:
│   │   ├─ Create prompt
│   │   ├─ POST to SD-XL API
│   │   ├─ Wait for response (30-60s)
│   │   └─ Store image
│   └─ Combine results
│
└─ 8. Display Results
    └─ Render in tabbed interface
```

---

## Error Handling Strategy

```
Error Handling Layers
│
├─ Input Validation
│   ├─ Check required fields
│   ├─ Validate data types
│   └─ Display user-friendly messages
│
├─ API Key Validation
│   ├─ Check environment variable
│   ├─ Verify key format
│   └─ Show setup instructions
│
├─ API Call Errors
│   ├─ Network errors
│   │   ├─ Retry with backoff
│   │   └─ Show connection message
│   │
│   ├─ 503 Service Unavailable
│   │   ├─ Model loading
│   │   ├─ Wait and retry
│   │   └─ Show loading message
│   │
│   ├─ Rate limiting
│   │   ├─ Detect limit errors
│   │   └─ Show wait message
│   │
│   └─ Timeout errors
│       ├─ Extend timeout
│       └─ Retry request
│
├─ Parsing Errors
│   ├─ Fallback values
│   ├─ Default content
│   └─ Log warnings
│
└─ Export Errors
    ├─ Validate data
    ├─ Handle encoding
    └─ Show error message
```

---

## Performance Optimization

```
Optimization Strategies
│
├─ Caching
│   ├─ Session state caching
│   ├─ Streamlit @cache_data
│   └─ Result persistence
│
├─ Parallel Processing
│   ├─ Independent API calls
│   └─ Async where possible
│
├─ Lazy Loading
│   ├─ Load images on demand
│   └─ Defer heavy operations
│
├─ Request Optimization
│   ├─ Batch similar requests
│   ├─ Minimize API calls
│   └─ Reuse connections
│
└─ UI Optimization
    ├─ Efficient rendering
    ├─ Minimal re-renders
    └─ Progressive loading
```

---

## Security Architecture

```
Security Layers
│
├─ Environment Variables
│   ├─ .env file (local)
│   ├─ Platform secrets (cloud)
│   └─ No hardcoded keys
│
├─ Input Sanitization
│   ├─ Validate user input
│   ├─ Prevent injection
│   └─ Limit input size
│
├─ API Security
│   ├─ HTTPS only
│   ├─ Token authentication
│   └─ Rate limiting
│
├─ Data Privacy
│   ├─ No data persistence
│   ├─ Session-only storage
│   └─ No logging of sensitive data
│
└─ Deployment Security
    ├─ .gitignore secrets
    ├─ Secure transmission
    └─ Access controls
```

---

## Scalability Considerations

```
Scaling Strategy
│
├─ Horizontal Scaling
│   ├─ Multiple instances
│   ├─ Load balancing
│   └─ Session management
│
├─ Vertical Scaling
│   ├─ Increase resources
│   ├─ Better hardware
│   └─ Optimize code
│
├─ Caching Layer
│   ├─ Redis integration
│   ├─ Result caching
│   └─ Reduce API calls
│
├─ Database Integration
│   ├─ Store projects
│   ├─ User management
│   └─ History tracking
│
└─ CDN Integration
    ├─ Static assets
    ├─ Image delivery
    └─ Global distribution
```

---

## Technology Stack Details

```
Technology Stack
│
├─ Frontend
│   ├─ Streamlit 1.31.0
│   ├─ Custom CSS
│   └─ HTML/JavaScript (embedded)
│
├─ Backend
│   ├─ Python 3.8+
│   ├─ Requests library
│   └─ Python-dotenv
│
├─ AI/ML
│   ├─ Hugging Face Hub
│   ├─ Mistral-7B-Instruct
│   └─ Stable Diffusion XL
│
├─ Image Processing
│   ├─ Pillow (PIL)
│   └─ BytesIO
│
├─ Export
│   ├─ FPDF (PDF generation)
│   └─ Text formatting
│
└─ Deployment
    ├─ Streamlit Cloud
    ├─ Hugging Face Spaces
    ├─ Docker
    └─ Cloud platforms
```

---

## Module Dependencies

```
Dependency Graph
│
app.py
├── utils.ai_generator
│   ├── requests
│   ├── time
│   ├── PIL
│   └── utils.prompts
│
├── utils.ui_components
│   └── streamlit
│
├── utils.exporter
│   ├── fpdf
│   └── io
│
├── streamlit
├── os
└── dotenv
```

---

## Deployment Architecture

```
Deployment Options
│
├─ Streamlit Cloud
│   ├─ Git integration
│   ├─ Automatic deployment
│   ├─ Built-in secrets
│   └─ Free tier available
│
├─ Hugging Face Spaces
│   ├─ Git-based deployment
│   ├─ Integrated with HF
│   ├─ GPU options
│   └─ Community visibility
│
├─ Heroku
│   ├─ Procfile configuration
│   ├─ Buildpack setup
│   ├─ Environment variables
│   └─ Custom domains
│
├─ AWS EC2
│   ├─ Ubuntu instance
│   ├─ Systemd service
│   ├─ Nginx reverse proxy
│   └─ Full control
│
└─ Docker
    ├─ Dockerfile
    ├─ Docker Compose
    ├─ Container orchestration
    └─ Portable deployment
```

---

## Future Architecture Enhancements

```
Planned Improvements
│
├─ Microservices
│   ├─ Separate AI service
│   ├─ Export service
│   └─ API gateway
│
├─ Database Layer
│   ├─ PostgreSQL
│   ├─ User projects
│   └─ History tracking
│
├─ Authentication
│   ├─ User accounts
│   ├─ OAuth integration
│   └─ Role-based access
│
├─ Real-time Features
│   ├─ WebSocket support
│   ├─ Live collaboration
│   └─ Progress streaming
│
└─ Advanced Caching
    ├─ Redis integration
    ├─ Distributed cache
    └─ Smart invalidation
```

---

**Architecture designed for scalability, maintainability, and performance** 🏗️

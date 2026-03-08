# 🔧 Scriptoria - API Reference

## AIGenerator Class

Main class for AI model interactions and content generation.

### Constructor

```python
AIGenerator(api_key: str)
```

**Parameters:**
- `api_key` (str): Hugging Face API token

**Example:**
```python
from utils.ai_generator import AIGenerator

api_key = "hf_your_token_here"
generator = AIGenerator(api_key)
```

---

## Methods

### generate_screenplay()

Generate a professional screenplay from story concept.

```python
generate_screenplay(
    title: str,
    concept: str,
    genre: str,
    duration: str
) -> str
```

**Parameters:**
- `title` (str): Film title
- `concept` (str): Story description
- `genre` (str): Film genre (Action, Drama, etc.)
- `duration` (str): "Short Film" or "Feature Film"

**Returns:**
- `str`: Formatted screenplay text

**Example:**
```python
screenplay = generator.generate_screenplay(
    title="The Last Signal",
    concept="A radio operator receives a mysterious signal...",
    genre="Sci-Fi",
    duration="Feature Film (90+ min)"
)
```

---

### generate_characters()

Generate detailed character profiles.

```python
generate_characters(
    concept: str,
    genre: str,
    num_characters: int
) -> List[Dict]
```

**Parameters:**
- `concept` (str): Story description
- `genre` (str): Film genre
- `num_characters` (int): Number of characters (1-10)

**Returns:**
- `List[Dict]`: List of character dictionaries

**Character Dictionary Structure:**
```python
{
    'name': str,
    'background': str,
    'personality': str,
    'motivation': str,
    'arc': str
}
```

**Example:**
```python
characters = generator.generate_characters(
    concept="A thriller about corporate espionage",
    genre="Thriller",
    num_characters=3
)

for char in characters:
    print(f"{char['name']}: {char['motivation']}")
```

---

### generate_sound_design()

Generate sound design suggestions for scenes.

```python
generate_sound_design(
    concept: str,
    genre: str
) -> List[Dict]
```

**Parameters:**
- `concept` (str): Story description
- `genre` (str): Film genre

**Returns:**
- `List[Dict]`: List of sound design dictionaries

**Sound Design Dictionary Structure:**
```python
{
    'scene': str,
    'music': str,
    'ambient': str,
    'emotional': str
}
```

**Example:**
```python
sound = generator.generate_sound_design(
    concept="A horror film in an abandoned hospital",
    genre="Horror"
)

for scene_sound in sound:
    print(f"{scene_sound['scene']}: {scene_sound['music']}")
```

---

### generate_budget()

Calculate production budget estimate.

```python
generate_budget(
    duration: str,
    num_characters: int
) -> Dict
```

**Parameters:**
- `duration` (str): Film duration
- `num_characters` (int): Number of characters

**Returns:**
- `Dict`: Budget breakdown dictionary

**Budget Dictionary Structure:**
```python
{
    'cast': int,
    'crew': int,
    'equipment': int,
    'locations': int,
    'sound': int,
    'post_production': int,
    'total': int
}
```

**Example:**
```python
budget = generator.generate_budget(
    duration="Feature Film (90+ min)",
    num_characters=5
)

print(f"Total Budget: ${budget['total']:,}")
print(f"Cast: ${budget['cast']:,}")
```

---

### generate_storyboard_images()

Generate AI storyboard images for key scenes.

```python
generate_storyboard_images(
    concept: str,
    genre: str
) -> List[Dict]
```

**Parameters:**
- `concept` (str): Story description
- `genre` (str): Film genre

**Returns:**
- `List[Dict]`: List of storyboard dictionaries

**Storyboard Dictionary Structure:**
```python
{
    'title': str,
    'image': PIL.Image or None,
    'camera': str,
    'lighting': str
}
```

**Example:**
```python
storyboard = generator.generate_storyboard_images(
    concept="An action sequence in a moving train",
    genre="Action"
)

for scene in storyboard:
    if scene['image']:
        scene['image'].save(f"{scene['title']}.png")
```

---

## Prompt Functions

Located in `utils/prompts.py`

### create_screenplay_prompt()

```python
create_screenplay_prompt(
    title: str,
    concept: str,
    genre: str,
    duration: str
) -> str
```

Creates optimized prompt for screenplay generation.

---

### create_character_prompt()

```python
create_character_prompt(
    concept: str,
    genre: str,
    character_num: int
) -> str
```

Creates prompt for character profile generation.

---

### create_sound_design_prompt()

```python
create_sound_design_prompt(
    concept: str,
    genre: str
) -> str
```

Creates prompt for sound design suggestions.

---

### create_storyboard_prompt()

```python
create_storyboard_prompt(
    scene_description: str,
    genre: str
) -> str
```

Creates optimized prompt for image generation.

---

## Export Functions

Located in `utils/exporter.py`

### export_screenplay()

```python
export_screenplay(project_data: Dict) -> str
```

**Parameters:**
- `project_data` (Dict): Complete project data

**Returns:**
- `str`: Formatted screenplay text

**Example:**
```python
from utils.exporter import export_screenplay

screenplay_txt = export_screenplay(project_data)
with open('screenplay.txt', 'w') as f:
    f.write(screenplay_txt)
```

---

### export_full_project()

```python
export_full_project(
    project_data: Dict,
    format: str = 'pdf'
) -> bytes
```

**Parameters:**
- `project_data` (Dict): Complete project data
- `format` (str): Export format ('pdf')

**Returns:**
- `bytes`: PDF file content

**Example:**
```python
from utils.exporter import export_full_project

pdf_bytes = export_full_project(project_data, format='pdf')
with open('project.pdf', 'wb') as f:
    f.write(pdf_bytes)
```

---

## UI Components

Located in `utils/ui_components.py`

### apply_custom_css()

```python
apply_custom_css() -> None
```

Applies custom CSS styling to Streamlit app.

**Usage:**
```python
from utils.ui_components import apply_custom_css

apply_custom_css()
```

---

### render_hero_section()

```python
render_hero_section() -> None
```

Renders the hero section with title and subtitle.

---

### render_feature_cards()

```python
render_feature_cards() -> None
```

Renders feature highlight cards.

---

## Project Data Structure

Complete project data dictionary structure:

```python
project_data = {
    'title': str,              # Film title
    'genre': str,              # Film genre
    'screenplay': str,         # Full screenplay text
    'characters': [            # List of characters
        {
            'name': str,
            'background': str,
            'personality': str,
            'motivation': str,
            'arc': str
        }
    ],
    'sound_design': [          # List of sound designs
        {
            'scene': str,
            'music': str,
            'ambient': str,
            'emotional': str
        }
    ],
    'budget': {                # Budget breakdown
        'cast': int,
        'crew': int,
        'equipment': int,
        'locations': int,
        'sound': int,
        'post_production': int,
        'total': int
    },
    'storyboard': [            # List of storyboard scenes
        {
            'title': str,
            'image': PIL.Image or None,
            'camera': str,
            'lighting': str
        }
    ]
}
```

---

## Error Handling

### Common Exceptions

**API Key Missing:**
```python
if not api_key:
    raise ValueError("HF_API_KEY not found in environment")
```

**API Request Failed:**
```python
try:
    response = requests.post(api_url, ...)
except Exception as e:
    raise Exception(f"API request failed: {str(e)}")
```

**Model Loading (503):**
```python
if response.status_code == 503:
    # Automatic retry with delay
    time.sleep(20)
```

---

## Configuration

### AI Model Settings

**Text Generation:**
```python
{
    "max_new_tokens": 2000,
    "temperature": 0.7,
    "top_p": 0.9,
    "return_full_text": False
}
```

**Image Generation:**
```python
{
    "inputs": prompt,
    # Stable Diffusion XL default settings
}
```

### Retry Settings

```python
max_retries = 3
retry_delay = 5  # seconds
model_loading_delay = 20  # seconds
```

---

## Usage Examples

### Complete Workflow

```python
import os
from dotenv import load_dotenv
from utils.ai_generator import AIGenerator
from utils.exporter import export_full_project

# Load environment
load_dotenv()
api_key = os.getenv("HF_API_KEY")

# Initialize generator
generator = AIGenerator(api_key)

# Generate content
screenplay = generator.generate_screenplay(
    "The Last Signal",
    "A radio operator receives a mysterious signal...",
    "Sci-Fi",
    "Feature Film (90+ min)"
)

characters = generator.generate_characters(
    "A radio operator receives a mysterious signal...",
    "Sci-Fi",
    3
)

sound = generator.generate_sound_design(
    "A radio operator receives a mysterious signal...",
    "Sci-Fi"
)

budget = generator.generate_budget(
    "Feature Film (90+ min)",
    3
)

storyboard = generator.generate_storyboard_images(
    "A radio operator receives a mysterious signal...",
    "Sci-Fi"
)

# Create project data
project_data = {
    'title': "The Last Signal",
    'genre': "Sci-Fi",
    'screenplay': screenplay,
    'characters': characters,
    'sound_design': sound,
    'budget': budget,
    'storyboard': storyboard
}

# Export
pdf_bytes = export_full_project(project_data)
with open('project.pdf', 'wb') as f:
    f.write(pdf_bytes)
```

---

## API Rate Limits

### Hugging Face Free Tier

- **Requests per hour:** ~1000
- **Concurrent requests:** Limited
- **Model loading:** First request may take 20-30s

### Optimization Tips

1. Cache results using `st.cache_data`
2. Batch similar requests
3. Implement exponential backoff
4. Monitor usage on HF dashboard

---

## Environment Variables

```bash
# Required
HF_API_KEY=your_hugging_face_token

# Optional (with defaults)
TEXT_MODEL=mistralai/Mistral-7B-Instruct-v0.1
IMAGE_MODEL=stabilityai/stable-diffusion-xl-base-1.0
MAX_RETRIES=3
REQUEST_TIMEOUT=60
```

---

## Testing

### Unit Test Example

```python
import unittest
from utils.ai_generator import AIGenerator

class TestAIGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = AIGenerator("test_key")
    
    def test_budget_calculation(self):
        budget = self.generator.generate_budget(
            "Feature Film (90+ min)",
            3
        )
        self.assertIn('total', budget)
        self.assertGreater(budget['total'], 0)

if __name__ == '__main__':
    unittest.main()
```

---

## Performance Metrics

### Typical Generation Times

| Component | Time | Model |
|-----------|------|-------|
| Screenplay | 10-20s | Mistral-7B |
| Character (each) | 5-10s | Mistral-7B |
| Sound Design | 8-15s | Mistral-7B |
| Budget | <1s | Calculation |
| Storyboard (each) | 30-60s | SD-XL |

**Total:** ~2-3 minutes for complete package

---

## Troubleshooting

### Debug Mode

Enable detailed logging:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# In your code
logger.debug(f"API Response: {response.status_code}")
```

### Common Issues

**Timeout Errors:**
```python
# Increase timeout
response = requests.post(api_url, timeout=120)
```

**Memory Issues:**
```python
# Clear Streamlit cache
st.cache_data.clear()
```

---

## Contributing

### Adding New Features

1. Create new function in appropriate module
2. Add to API reference
3. Update tests
4. Document usage

### Code Style

- Follow PEP 8
- Use type hints
- Add docstrings
- Include examples

---

**For more information, see the main README.md**

import requests
import time
from io import BytesIO
from PIL import Image
from .prompts import (
    create_screenplay_prompt,
    create_character_prompt,
    create_sound_design_prompt,
    create_storyboard_prompt
)

class AIGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.text_model = "mistralai/Mistral-7B-Instruct-v0.1"
        self.image_model = "stabilityai/stable-diffusion-xl-base-1.0"
        self.headers = {"Authorization": f"Bearer {api_key}"}
    
    def _call_text_api(self, prompt, max_tokens=2000):
        """Call Hugging Face text generation API"""
        api_url = f"https://api-inference.huggingface.co/models/{self.text_model}"
        
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_tokens,
                "temperature": 0.7,
                "top_p": 0.9,
                "return_full_text": False
            }
        }
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(api_url, headers=self.headers, json=payload, timeout=60)
                
                if response.status_code == 503:
                    # Model is loading
                    time.sleep(20)
                    continue
                
                response.raise_for_status()
                result = response.json()
                
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', '')
                return str(result)
                
            except Exception as e:
                if attempt == max_retries - 1:
                    raise Exception(f"Text generation failed: {str(e)}")
                time.sleep(5)
        
        return "Error generating content. Please try again."
    
    def _call_image_api(self, prompt):
        """Call Hugging Face image generation API"""
        api_url = f"https://api-inference.huggingface.co/models/{self.image_model}"
        
        payload = {"inputs": prompt}
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(api_url, headers=self.headers, json=payload, timeout=120)
                
                if response.status_code == 503:
                    # Model is loading
                    time.sleep(30)
                    continue
                
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
                return image
                
            except Exception as e:
                if attempt == max_retries - 1:
                    return None
                time.sleep(10)
        
        return None
    
    def generate_screenplay(self, title, concept, genre, duration):
        """Generate screenplay from story concept"""
        prompt = create_screenplay_prompt(title, concept, genre, duration)
        screenplay = self._call_text_api(prompt, max_tokens=2500)
        return screenplay
    
    def generate_characters(self, concept, genre, num_characters):
        """Generate character profiles"""
        characters = []
        
        for i in range(num_characters):
            prompt = create_character_prompt(concept, genre, i + 1)
            char_text = self._call_text_api(prompt, max_tokens=500)
            
            # Parse character details
            character = self._parse_character(char_text, i + 1)
            characters.append(character)
        
        return characters
    
    def _parse_character(self, text, index):
        """Parse character text into structured format"""
        lines = text.split('\n')
        
        character = {
            'name': f"Character {index}",
            'background': "",
            'personality': "",
            'motivation': "",
            'arc': ""
        }
        
        current_field = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            lower_line = line.lower()
            if 'name:' in lower_line or 'character' in lower_line:
                character['name'] = line.split(':', 1)[-1].strip() or f"Character {index}"
                current_field = 'name'
            elif 'background:' in lower_line:
                character['background'] = line.split(':', 1)[-1].strip()
                current_field = 'background'
            elif 'personality:' in lower_line:
                character['personality'] = line.split(':', 1)[-1].strip()
                current_field = 'personality'
            elif 'motivation:' in lower_line:
                character['motivation'] = line.split(':', 1)[-1].strip()
                current_field = 'motivation'
            elif 'arc:' in lower_line or 'emotional arc:' in lower_line:
                character['arc'] = line.split(':', 1)[-1].strip()
                current_field = 'arc'
            elif current_field and ':' not in line:
                character[current_field] += " " + line
        
        # Fallback values
        if not character['background']:
            character['background'] = "A complex character with a mysterious past."
        if not character['personality']:
            character['personality'] = "Determined, resourceful, and emotionally layered."
        if not character['motivation']:
            character['motivation'] = "Seeking truth and redemption."
        if not character['arc']:
            character['arc'] = "Transforms from uncertainty to self-discovery."
        
        return character
    
    def generate_sound_design(self, concept, genre):
        """Generate sound design suggestions"""
        prompt = create_sound_design_prompt(concept, genre)
        sound_text = self._call_text_api(prompt, max_tokens=800)
        
        # Parse into scenes
        sound_design = []
        scenes = sound_text.split('\n\n')
        
        for idx, scene in enumerate(scenes[:5], 1):
            if scene.strip():
                sound_design.append({
                    'scene': f"Scene {idx}",
                    'music': self._extract_field(scene, 'music') or "Atmospheric orchestral score",
                    'ambient': self._extract_field(scene, 'ambient') or "Natural environmental sounds",
                    'emotional': self._extract_field(scene, 'emotional') or "Building tension and anticipation"
                })
        
        if not sound_design:
            sound_design = [{
                'scene': 'Opening Scene',
                'music': 'Atmospheric orchestral score with subtle tension',
                'ambient': 'Natural environmental sounds, distant city noise',
                'emotional': 'Building anticipation and mystery'
            }]
        
        return sound_design
    
    def _extract_field(self, text, field):
        """Extract specific field from text"""
        lines = text.lower().split('\n')
        for line in lines:
            if field in line and ':' in line:
                return line.split(':', 1)[-1].strip()
        return None
    
    def generate_budget(self, duration, num_characters):
        """Generate production budget estimate"""
        is_feature = "Feature" in duration
        
        base_multiplier = 2.5 if is_feature else 1.0
        char_multiplier = num_characters * 0.3
        
        budget = {
            'cast': int(15000 * base_multiplier * (1 + char_multiplier)),
            'crew': int(25000 * base_multiplier),
            'equipment': int(20000 * base_multiplier),
            'locations': int(10000 * base_multiplier),
            'sound': int(8000 * base_multiplier),
            'post_production': int(18000 * base_multiplier)
        }
        
        budget['total'] = sum(budget.values())
        
        return budget
    
    def generate_storyboard_images(self, concept, genre):
        """Generate storyboard images for key scenes"""
        storyboard = []
        
        # Generate 3 key scenes
        scene_descriptions = [
            f"Opening scene: {concept[:100]}",
            f"Mid-point tension: {genre} film dramatic moment",
            f"Climactic finale: {genre} film resolution"
        ]
        
        scene_titles = ["Opening Scene", "Mid-Point", "Climax"]
        camera_angles = ["Wide establishing shot", "Medium close-up", "Dynamic action shot"]
        lighting = ["Natural daylight", "Dramatic low-key lighting", "High contrast lighting"]
        
        for idx, (desc, title, camera, light) in enumerate(zip(scene_descriptions, scene_titles, camera_angles, lighting)):
            prompt = create_storyboard_prompt(desc, genre)
            image = self._call_image_api(prompt)
            
            storyboard.append({
                'title': title,
                'image': image,
                'camera': camera,
                'lighting': light
            })
        
        return storyboard

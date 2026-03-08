def create_screenplay_prompt(title, concept, genre, duration):
    """Create prompt for screenplay generation"""
    is_short = "Short" in duration
    
    prompt = f"""Write a professional {genre} screenplay titled "{title}".

Story Concept: {concept}

Format: {"Short film (20-30 pages)" if is_short else "Feature film (90-120 pages)"}

Create a properly formatted screenplay with:
- Scene headings (INT./EXT. LOCATION - TIME)
- Character names in CAPS
- Action descriptions
- Dialogue
- Camera directions where appropriate

Write the opening 3-5 scenes of this screenplay in professional format.

Screenplay:"""
    
    return prompt

def create_character_prompt(concept, genre, character_num):
    """Create prompt for character generation"""
    prompt = f"""Create a detailed character profile for a {genre} film.

Story Context: {concept}

Generate Character #{character_num} with the following details:

Name: [Character name]
Background: [Character's history and background]
Personality: [Key personality traits]
Motivation: [What drives this character]
Emotional Arc: [How the character changes throughout the story]

Provide detailed, cinematic character description:"""
    
    return prompt

def create_sound_design_prompt(concept, genre):
    """Create prompt for sound design suggestions"""
    prompt = f"""Create sound design suggestions for a {genre} film.

Story: {concept}

For each major scene, provide:
- Music style and instrumentation
- Ambient sound effects
- Emotional sound cues

Generate sound design for 3-5 key scenes:

Scene 1:
Music: [description]
Ambient: [description]
Emotional: [description]

Continue for remaining scenes..."""
    
    return prompt

def create_storyboard_prompt(scene_description, genre):
    """Create prompt for storyboard image generation"""
    prompt = f"""Cinematic film still, {genre} movie scene, {scene_description}, 
    professional cinematography, dramatic lighting, film grain, 
    high quality, movie production, cinematic composition, 
    detailed environment, atmospheric"""
    
    return prompt

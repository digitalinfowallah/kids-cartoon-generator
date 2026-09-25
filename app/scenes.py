def create_scenes(story, characters):
    """
    Create scenes for the cartoon video.
    """

    scenes = []

    for scene in story.get("scenes", []):
        scenes.append({
            "scene_number": scene["scene"],
            "description": scene["description"],
            "dialogue": scene["dialogue"],
            "duration": scene["duration"],
            "characters": characters
        })

    return scenes

def generate_sound_effects(scene):
    """
    Prepare sound effects for one cartoon scene.

    The real AI sound-effects service will be connected later.
    """

    return {
        "scene": scene,
        "effects": [
            "pop",
            "whoosh",
            "happy_chime"
        ],
        "audio_file": None,
        "status": "ready"
    }

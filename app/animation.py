def generate_animation(scene, characters, style="3D Cartoon"):
    """
    Generate cartoon animation for one scene.

    The real AI animation service will be connected later.
    """

    animation = {
        "scene": scene,
        "characters": characters,
        "style": style,
        "status": "ready",
        "video_file": None
    }

    return animation

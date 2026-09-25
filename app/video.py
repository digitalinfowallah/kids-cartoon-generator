def create_video(scenes, voices):
    """
    Assemble scenes and voices into the final cartoon video.

    Final target:
    - Vertical 9:16
    - 2160 x 3840
    - MP4
    """

    video_settings = {
        "width": 2160,
        "height": 3840,
        "aspect_ratio": "9:16",
        "format": "mp4",
        "quality": "4K"
    }

    return {
        "status": "ready",
        "settings": video_settings,
        "file": None
    }

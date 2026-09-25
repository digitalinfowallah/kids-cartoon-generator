def create_subtitles(scenes):
    """
    Create subtitles for the cartoon scenes.
    """

    subtitles = []

    for scene in scenes:

        subtitles.append({
            "scene": scene["scene_number"],
            "text": scene["dialogue"],
            "start": 0,
            "end": scene["duration"]
        })

    return subtitles

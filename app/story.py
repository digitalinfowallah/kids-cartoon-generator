def create_story(user_idea, language="English"):
    """
    Convert a simple idea into a structured kids cartoon story.
    """

    story = {
        "title": "My Kids Cartoon",
        "language": language,
        "idea": user_idea,
        "scenes": [
            {
                "scene": 1,
                "description": user_idea,
                "dialogue": "",
                "duration": 5
            }
        ]
    }

    return story

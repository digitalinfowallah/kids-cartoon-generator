import json
import os
import subprocess


def create_story(user_idea, language="English"):
    """
    Generate a kids cartoon story.

    Uses a local Ollama model when available.
    Falls back to a simple story if Ollama is not running.
    """

    prompt = f"""
Create a short, child-friendly cartoon story.

Story idea:
{user_idea}

Language:
{language}

Create 5 short scenes.

Return ONLY valid JSON:

{{
    "title": "story title",
    "scenes": [
        {{
            "scene": 1,
            "description": "scene description",
            "dialogue": "spoken dialogue",
            "duration": 6
        }}
    ]
}}

Rules:
- Suitable for children.
- Positive and educational.
- Simple language.
- Visually interesting.
- No violence.
- No frightening content.
"""

    try:
        result = subprocess.run(
            [
                "ollama",
                "run",
                "llama3.2:3b",
                prompt
            ],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0:
            content = result.stdout.strip()

            story = json.loads(content)

            story["language"] = language
            story["idea"] = user_idea

            return story

    except Exception:
        pass


    # Free fallback
    return {
        "title": "My Kids Cartoon",
        "language": language,
        "idea": user_idea,
        "scenes": [
            {
                "scene": 1,
                "description": user_idea,
                "dialogue": (
                    "Let's go on a wonderful adventure!"
                ),
                "duration": 6
            },
            {
                "scene": 2,
                "description": (
                    "The main character discovers "
                    "something interesting."
                ),
                "dialogue": (
                    "Wow! Look what I found!"
                ),
                "duration": 6
            },
            {
                "scene": 3,
                "description": (
                    "The character learns an important lesson."
                ),
                "dialogue": (
                    "Now I understand!"
                ),
                "duration": 6
            },
            {
                "scene": 4,
                "description": (
                    "The character shares the lesson "
                    "with friends."
                ),
                "dialogue": (
                    "We can all help each other!"
                ),
                "duration": 6
            },
            {
                "scene": 5,
                "description": (
                    "Everyone celebrates together."
                ),
                "dialogue": (
                    "What a wonderful day!"
                ),
                "duration": 6
            }
        ]
    }

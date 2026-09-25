import streamlit as st

from story import create_story
from characters import create_characters
from scenes import create_scenes
from voice import generate_voice
from video import create_video


st.set_page_config(
    page_title="AI Kids Cartoon Maker",
    page_icon="🎬",
    layout="centered"
)


st.title("🎨 AI Kids Cartoon Maker")

st.write(
    "Create a kids cartoon video automatically with one click."
)


story_idea = st.text_area(
    "📝 Enter your story",
    placeholder="Example: A little rabbit learns to share his toys with his friends.",
    height=150
)


language = st.selectbox(
    "🌐 Language",
    ["English", "Hindi"]
)


style = st.selectbox(
    "🎨 Cartoon Style",
    [
        "3D Cartoon",
        "2D Cartoon",
        "Cute Cartoon"
    ]
)


voice = st.selectbox(
    "🎙️ Voice",
    [
        "Friendly Narrator",
        "Funny Cartoon",
        "Child Friendly"
    ]
)


if st.button(
    "🎬 GENERATE VIDEO",
    type="primary",
    use_container_width=True
):

    if not story_idea.strip():

        st.error("Please enter a story first.")

    else:

        progress = st.progress(0)

        status = st.empty()


        # Step 1: Create story
        status.write("📝 Creating story...")
        story = create_story(
            story_idea,
            language
        )
        progress.progress(20)


        # Step 2: Create characters
        status.write("🐰 Creating cartoon characters...")
        characters = create_characters(story)
        progress.progress(40)


        # Step 3: Create scenes
        status.write("🎬 Creating scenes...")
        scenes = create_scenes(
            story,
            characters
        )
        progress.progress(55)


        # Step 4: Generate voice
        status.write("🎙️ Preparing character voices...")

        voices = []

        for scene in scenes:

            voice_data = generate_voice(
                scene["dialogue"],
                voice,
                language
            )

            voices.append(voice_data)

        progress.progress(70)


        # Step 5: Create video
        status.write("🎞️ Preparing 9:16 4K video...")

        video = create_video(
            scenes,
            voices
        )

        progress.progress(100)


        status.success(
            "🎉 Cartoon video generation pipeline completed!"
        )


        st.subheader("📋 Video Settings")

        st.write(
            f"Resolution: "
            f"{video['settings']['width']} × "
            f"{video['settings']['height']}"
        )

        st.write(
            f"Aspect Ratio: "
            f"{video['settings']['aspect_ratio']}"
        )

        st.write(
            f"Format: "
            f"{video['settings']['format']}"
        )

        st.write(
            f"Quality: "
            f"{video['settings']['quality']}"
        )

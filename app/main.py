import streamlit as st

from story import create_story
from characters import create_characters
from scenes import create_scenes
from voice import generate_voice
from video import create_video

from animation import generate_animation
from music import generate_music
from effects import generate_sound_effects
from subtitles import create_subtitles
from renderer import render_video


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
    placeholder=(
        "Example: A little rabbit learns to share "
        "his toys with his friends."
    ),
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

        progress.progress(10)


        # Step 2: Create characters
        status.write("🐰 Creating cartoon characters...")

        characters = create_characters(
            story
        )

        progress.progress(20)


        # Step 3: Create scenes
        status.write("🎬 Creating scenes...")

        scenes = create_scenes(
            story,
            characters
        )

        progress.progress(30)


        # Step 4: Generate animation
        status.write("🎞️ Creating cartoon animation...")

        animations = []

        for scene in scenes:

            animation = generate_animation(
                scene,
                characters,
                style
            )

            animations.append(animation)

        progress.progress(45)


        # Step 5: Generate voices
        status.write("🎙️ Preparing character voices...")

        voices = []

        for scene in scenes:

            voice_data = generate_voice(
                scene["dialogue"],
                voice,
                language
            )

            voices.append(voice_data)

        progress.progress(55)


        # Step 6: Generate music
        status.write("🎵 Preparing background music...")

        music = generate_music(
            style
        )

        progress.progress(65)


        # Step 7: Generate sound effects
        status.write("🔊 Preparing sound effects...")

        effects = []

        for scene in scenes:

            sound_effects = generate_sound_effects(
                scene
            )

            effects.append(sound_effects)

        progress.progress(72)


        # Step 8: Create subtitles
        status.write("📝 Creating subtitles...")

        subtitles = create_subtitles(
            scenes
        )

        progress.progress(80)


        # Step 9: Render final video
        status.write(
            "🎞️ Rendering 9:16 4K cartoon video..."
        )

        final_video = render_video(
            scenes,
            animations,
            voices,
            music,
            effects,
            subtitles
        )

        progress.progress(95)


        # Legacy video settings
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
            f"{final_video['settings']['width']} × "
            f"{final_video['settings']['height']}"
        )

        st.write(
            f"Aspect Ratio: "
            f"{final_video['settings']['aspect_ratio']}"
        )

        st.write(
            f"Format: "
            f"{final_video['settings']['format']}"
        )

        st.write(
            f"Quality: "
            f"{final_video['settings']['quality']}"
        )

        st.info(
            "The current version contains the complete "
            "generation pipeline structure. AI generation "
            "and real video rendering APIs will be connected next."
        )

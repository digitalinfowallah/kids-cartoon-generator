import streamlit as st

st.set_page_config(
    page_title="AI Kids Cartoon Maker",
    page_icon="🎬",
    layout="centered"
)

st.title("🎨 AI Kids Cartoon Maker")

st.write("Create a cartoon video automatically with one click.")

story = st.text_area(
    "📝 Enter your story",
    placeholder="Example: A little rabbit goes on an adventure...",
    height=150
)

language = st.selectbox(
    "🌐 Language",
    ["English", "Hindi"]
)

style = st.selectbox(
    "🎨 Cartoon Style",
    ["3D Cartoon", "2D Cartoon", "Cute Cartoon"]
)

voice = st.selectbox(
    "🎙️ Voice",
    ["Friendly Narrator", "Funny Cartoon", "Child Friendly"]
)

if st.button(
    "🎬 GENERATE VIDEO",
    type="primary",
    use_container_width=True
):
    if not story.strip():
        st.error("Please enter a story first.")
    else:
        st.success("🎉 Video generation started!")
        st.info("Our AI video pipeline will be connected in the next steps.")

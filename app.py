import streamlit as st import yaml from core.script_engine import generate_script from core.video_assembly import VideoAssembler

st.set_page_config(page_title="Staqlt AI Video Factory", layout="wide")

st.title("🎬 AI Video Production Pipeline")

with st.sidebar: st.header("Project Settings") video_ratio = st.selectbox("Aspect Ratio", ["9:16 (TikTok)", "16:9 (YouTube)"]) llm_model = st.selectbox("Script Model", ["Gemini 1.5 Pro", "GPT-4o"])

prompt = st.text_area("Enter your video concept/hook:")

if st.button("Generate Script & Scenes"): with st.spinner("Generating viral script..."): scenes = generate_script(prompt, llm_model) st.session_state['scenes'] = scenes st.success("Script generated!")

if 'scenes' in st.session_state: for i, scene in enumerate(st.session_state['scenes']): cols = st.columns([2, 1]) with cols[0]: st.text_area(f"Scene {i+1} Script", value=scene['text'], key=f"text_{i}") with cols[1]: st.button("Generate Motion", key=f"gen_{i}")

if st.button("🚀 Render Final Video"): assembler = VideoAssembler() output_path = assembler.build_video(st.session_state['scenes']) st.video(output_path)
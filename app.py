
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Little Runner",
    page_icon="🎮",
    layout="wide",
)

st.title("🎮 Little Runner")
st.write("Nhấn Space hoặc phím ↑ để nhảy qua chướng ngại vật.")

game_file = Path(__file__).parent / "index.html"

if game_file.exists():
    html = game_file.read_text(encoding="utf-8")
    components.html(
        html,
        height=470,
        scrolling=False,
    )
else:
    st.error("Không tìm thấy file index.html!")


import streamlit as st

st.set_page_config(
    page_title="Movie Recap Myanmar",
    page_icon="🎬"
)

st.title("🎬 Movie Recap Myanmar")
st.write("မြန်မာနှင့် အင်္ဂလိပ် Movie Recap App")

video_url = st.text_input(
    "YouTube Video Link ထည့်ပါ",
    placeholder="https://www.youtube.com/watch?v=..."
)

language = st.selectbox(
    "Recap ဘာသာစကားရွေးပါ",
    ["မြန်မာ", "English", "မြန်မာ + English"]
)

subtitle = st.multiselect(
    "စာတန်းထိုးရွေးပါ",
    ["မြန်မာစာတန်းထိုး", "English Subtitle"],
    default=["မြန်မာစာတန်းထိုး"]
)

if st.button("🎬 Create Movie Recap"):
    if video_url.strip():
        st.info("Video Link လက်ခံရရှိပါပြီ။")
        st.write("ရွေးထားသောဘာသာစကား:", language)
        st.write("စာတန်းထိုး:", ", ".join(subtitle))
        st.warning(
            "နောက်တစ်ဆင့်တွင် Video Captions ရယူခြင်း၊ "
            "Recap နှင့် အသံဖန်တီးခြင်းကို ထည့်ပါမည်။"
        )
    else:
        st.error("Video Link အရင်ထည့်ပါ။")
      

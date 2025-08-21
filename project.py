import streamlit as st
import time
import random

# Page config
st.set_page_config(page_title="Celebration!", page_icon="🎉", layout="centered")

# Title
st.title("🎉 It's a Boy! 💙")

# Balloons animation
st.balloons()

# Some fun messages in colors
colors = ["red", "blue", "green", "orange", "purple", "pink", "cyan"]

for i in range(20):
    color = random.choice(colors)
    st.markdown(f"<h2 style='color:{color};text-align:center;'>💙 It's a Boy! 💙</h2>", unsafe_allow_html=True)
    time.sleep(0.2)

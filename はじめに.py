import streamlit as st
import glob
from PIL import Image

st.title('さほのえいご学習')
st.subheader(":blue[さあ、今日もがんばりましょう]")

img = Image.open('./english_study_ver2/data/english_pic.jpg')
st.image(img,width=900)

st.markdown("""
            ### ファイト！　## ファイト！！　# ファイト！！！
            """)

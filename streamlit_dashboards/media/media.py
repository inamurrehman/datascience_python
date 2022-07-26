import streamlit as st
from PIL import Image

st.write('''
# Add media files in streamlit web app

''')

# Add image
st.write('''
    ## Image
''')
img1 = Image.open('inam.jpg')
st.image(img1)

# Add video
st.write('''
    ## Video
''')
video1 = open('tom.mp4', 'rb')
st.video(video1)

# Add audio
st.write('''
    ## Audio
''')
audio1 = open('Be.mp3', 'rb')
st.audio(audio1)
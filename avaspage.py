import streamlit as st


st.title(" Avas project page")

teachers_name = st.text_input(" enter your name")

picture = st.camera_input(" take a picture of your camera")


# audio = st.audio_input(" record your favourite song: ", max_duration=30)




if teachers_name :
    st.subheader(" Profile Name")
    st.write(teachers_name)


if teachers_name :
    st.subheader(" Profile picture")
    st.image(picture)


# if teachers_name :
#     st.subheader(" Favourite song")
#     st.audio(audio)
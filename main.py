import streamlit as st
from streamlit_lottie import st_lottie
import json


def load_lottieurl(path):
    with open(path) as f:
        return json.load(f)


lottie_coding = load_lottieurl("resources/lottie/ai_animation.json")

st.set_page_config(page_title="HuyWang Website", page_icon=":smiley:",
                   layout="wide", initial_sidebar_state="expanded")


# Header Section
with st.container():
    introduce_column, lottie_column = st.columns(2)
    with introduce_column:
        st.title("Hi I am HuyWang :wave:")
        st.write(
            "My name is Nguyen Huy Quang. People call me HuyWang so you can call me that too :smiley: i create this website for my portfolio :robot_face:")
    with lottie_column:
        st_lottie(lottie_coding, speed=1, height=200, key="initial")

# About Section
st.write("---")
st.title("About me")
st.subheader("Who am I?")
st.write(
    "I am interested in AI and Machine Learning. I am currently working as a AI developer at [ATIN Inovation](https://atin.com.vn)\n"
)

st.subheader("What I do?")
st.write("Find solutions to problems using AI and Machine Learning. Develop AI products for customers.")

st.subheader("What I have done?")
# st.write("I have done:")
st.write("- AI for smart parking system")
st.write("- AI for smart traffic system")
st.write("- AI for face recognition system")

st.subheader("More information?")
st.download_button("Download my CV", "resources/cv.pdf")

# Project Section
with open("resources/project.json") as f:
    project_list = json.load(f)

st.write("---")
st.title("My Projects")
for project in project_list:
    with st.container():
        image_column, text_column = st.columns([1, 4])
        with image_column:
            st.image(project["image"])
        with text_column:
            st.subheader(project["name"])
            st.write(project["description"])
            st.write("[Watch Demo]({})".format(project["url"]))
        st.write("\n")

# Footer Section
st.write("---")
st.title("Message me")
your_name = st.text_input("Your Name", placeholder="Your Name")
your_email = st.text_input("Your Email", placeholder="Your Email")
your_message = st.text_area("Your Message", placeholder="Your Message")
if st.button("Send"):
    if your_name and your_email and your_message:
        st.success("Thanks for your message!")
    else:
        st.error("Please fill in all fields!")

st.write("---")

st.write(":e-mail: huyquangbka@gmail.com")
st.write(":link: [Github](https://github.com/huyquang-bka)")
st.write(":telephone_receiver: +84 985 781 815")
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import json


def load_lottieurl(path):
    with open(path) as f:
        return json.load(f)


embedded_linkedin = {
    "linkedin": """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
    <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="huy-quang-nguyen-559879209" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://vn.linkedin.com/in/huy-quang-nguyen-559879209?trk=profile-badge">Huy Quang Nguyen</a></div>
    data-rss=
              """}


lottie_coding = load_lottieurl("resources/lottie/ai_animation.json")

st.set_page_config(page_title="HuyWang Website", page_icon=":robot_face:",
                   layout="wide", initial_sidebar_state="expanded")


# Header Section
with st.container():
    introduce_column, lottie_column = st.columns(2)
    with introduce_column:
        st.title("Hi I am HuyWang, an AI engineer :wave:")
    with lottie_column:
        st_lottie(lottie_coding, speed=1, height=200, key="initial")

# About Section
st.write("---")
st.title("About me")
st.subheader("Who am I?")
st.write(
    "I am an AI Engineer with 2 years of experience. I am currently working as an AI developer at [![ATIN](https://atin.com.vn/images/logo/3.png)](https://atin.com.vn)"
)

st.subheader("What I do?")
st.write("Find solutions to problems using AI and Machine Learning. Develop AI products for customers.")

st.subheader("What I have done?")
# st.write("I have done:")
st.write("- Smart parking system")
st.write("- Smart traffic system")
st.write("- Face recognition system")

st.subheader("More about my skills?")

# github
git_html = """<a href="https://github.com/huyquang-bka">
  <img src="https://cdn-icons-png.flaticon.com/128/5968/5968866.png" alt="Icon" style="width:50px;height:50px;">
</a>
"""
st.markdown(git_html, unsafe_allow_html=True)
#
st.write("\n")
# linkedin
linkedin_html = """<a href="https://www.linkedin.com/in/huy-quang-nguyen-559879209/">
  <img src="https://cdn-icons-png.flaticon.com/128/3536/3536505.png" alt="Icon" style="width:50px;height:50px;">
</a>
"""
st.markdown(linkedin_html, unsafe_allow_html=True)

st.write("\n")
# Download CV Section
# st.download_button(label="Download CV", file_name="Huy Quang CV.pdf",
#                    data=open("resources/CV.pdf", "rb").read())

# Archive Section
st.write("---")
st.title("My Archivement")
st.write("##")
st.subheader("Scientific Research Competition")
st.write("3rd Prize in Scientific Research of Hanoi University of Science & Technology 2020")

st.write("##")
st.subheader("ICCE 2020 paper")
st.write("[A Novel Method for Quantification of Vacant Parking Spaces at On-Street Parking Lots](https://ieeexplore.ieee.org/document/9852046)")

# Project Section
with open("resources/project.json") as f:
    project_list = json.load(f)

st.write("---")
st.title("My Projects")
for project in project_list:
    with st.container():
        image_column, text_column = st.columns([1, 3])
        with image_column:
            st.image(project["image"])
        with text_column:
            st.subheader(project["name"])
            st.write(project["description"])
            st.write("[Watch Demo]({})".format(project["url"]))
        st.write("##")

# Footer Section
st.write("---")
with st.container():
    message_column, _, contact_column = st.columns([2, 1, 2])
    with message_column:
        st.title("Message me")
        your_name = st.text_input("Your Name", placeholder="Your Name")
        your_email = st.text_input("Your Email", placeholder="Your Email")
        your_message = st.text_area("Your Message", placeholder="Your Message")
        if st.button("Send"):
            if your_name and your_email and your_message:
                st.success("Thanks for your message!")
            else:
                st.error("Please fill in all fields!")

    with contact_column:
        st.title("Contact me")
        st.subheader(":e-mail: huyquangbka@gmail.com")
        st.subheader(":telephone_receiver: +84 985 781 815")

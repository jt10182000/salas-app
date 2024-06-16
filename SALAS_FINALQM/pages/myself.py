import streamlit as st

st.title("EVERYTHING ABOUT ME📖👩👈")



st.title("📷PORTRAIT")


image_paths = ["pictures\me2.png"]


st.header(" SALAS, LYCA MAE")

st.markdown("""
##### 👨‍👩‍👧‍👦Family Members👨‍👩‍👧‍👦 

* 👩‍👦 Mother's Name: Donna Lyn B. Dumdumaya
* 👨‍👧‍👧 Father's Name: Erwin D. Dumdumaya

### 🔎 Overview
""", unsafe_allow_html=True)

# Personal Information
st.header("Personal Information")
st.write("**NAME:** LYCA MAE SALAS")
st.write("**AGE:** 21 YEARS OLD")
st.write("**EDUCATION:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**COURSE AND YEAR:** 3rd year Bachelor of Science in Information Systems Student")

with st.expander("GET TO KNOW ME BETTER 🌸"):
    st.markdown("""
    
    #
As an introverted person, I often struggle with the pressure of being the only child and the breadwinner of my family. 
I find it challenging to bond with my superficial friends and yearn for genuine connections. 
Despite these challenges, I am committed to balancing my responsibilities while ensuring I take care of my own well-being.
                
    """, unsafe_allow_html=True)

st.header("Hobbies")
st.write("1. *\"Playing Badminton\"*")
st.write("2. *\"Watch Kdarams and Anime, Sapphic Love Story\"*")

st.header("Favorite Food")
st.write("1. *\"Mango Sticky Rice\"*")
st.write("2. *\"Carbonara\"*")
st.write("3. *\"Adobo\"*")

st.header("Favorite Songs")
st.write("1. *\"Tell Me It's not a Dream\"*")
st.write("2. *\"My Kink is Karma\"*")

st.header("Life Lessons")
st.write("1. *\"Find strenght in your alone time and seek out genuine friendshipd over fake ones.\"*")
st.write("2. *\"Set boundaries to protect your well-being; It is okay to say no sometimes.\"*")
st.write("3. *\"While being the breadwinner is tough,taking care of yourself is just as important.\"*")



import streamlit as st


images = [
    {"path": ".itqmt\pict\friend3.jpg", "caption": "Academic years are often described as some of the most formative and challenging times in a person's life. The journey through education is filled with hurdles, demanding tasks, and moments of self-doubt. However, amidst the pressures of exams, projects, and deadlines, the presence of supportive friends and classmates plays an important role in not only making the experience bearable but also enriching and enjoyable.From the very first day of school, friendships begin to form. These bonds, initially built on shared classes and common interests, soon evolve into deeper relationships that provide a reliable support system. Friends and classmates become a source of encouragement, helping each other navigate through the hardship of academic life. Whether it's offering a listening ear after a tough day, sharing notes for a missed lecture, or providing motivation before a big exam, their presence is invaluable."},
    {"path": ".pictures\fr2.JPG", "caption": "We didn't realize we were making memories; we just knew we were having fun."},
    {"path": ".pictures/fr1.jpg", "caption": "A friend is one that knows you as you are, understands where you have been, accepts what you have become, and still, gently allows you to grow."},
    {"path": ".pictures\bff.png", "caption": "Best friends are the people who make your problems their problems, just so you don't have to go through them alone."},
    {"path": ".pictures\fam.jpg", "caption": "Behind every young child who believes in themselves is a parent who believed first."}
]


st.title("🖼️ MY COLLECTION OF MEMORIES")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: #F3F7EC;
        padding: 2em;
    }
    h1, h2 {
        color: #005C78;
    }
    .stText {
        font-size: 1.5em;
        color: #005C78;
    }
    </style>
    """,
    unsafe_allow_html=True
)

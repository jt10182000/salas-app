
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT: MACHINE LEARNING APPLICATIONS"),
        Section("MAIN PAGE"),
        Page("pages/aboutme.py", "👩‍💻 EVERYTHING ABOUT ME", "1️⃣", in_section=True),
        Page("pages/description.py", "📋 APP SPECIFICATION", "2️⃣", in_section=True),
        Page("pages/learnings.py", "📚🔍 LEARNINGS", "3️⃣", in_section=True),

        Section("APPLICATION PROJECT", "📂"),
        Page("pages/emotion.py", "😊 SENTIMENT ANALYZER", "1️⃣", in_section=True),
        Page("pages/classifyimage.py", "🖼️ ROOM CLASSIFICATION", "2️⃣", in_section=True),
        Page("pages/prediction.py", "🔮 PREDICTION", "3️⃣", in_section=True),

        Section("SOURCE CODE", "💻"),
        Page("pages/emotionsentimentanalyzer_src.py", "📄 SENTIMENT ANALYZER SRC", "1️⃣", in_section=True),
        Page("pages/classifyimage_src.py", "📄 ROOM CLASSIFICATION SRC", "2️⃣", in_section=True),
        Page("pages/prediction_src.py", "📄 PREDICTION SRC", "3️⃣", in_section=True),

        
    ]
)

hide_pages(["Thank you"])
st.markdown("---")

st.header("LYCA MAE SALAS")
st.image(".pictures/me.png")

st.markdown("---")

with st.expander("ALL ABOUT MACHINE LEARNING:"""):
    st.markdown("""
    
    #

        Machine Learning
             Machine learning is a type of artificial intelligence that helps systems learn and improve from experience without needing to be explicitly programmed. 
            It uses algorithms and statistical models to find patterns in data and make predictions or decisions based on those patterns. 
            Machine learning involves creating models that can handle large amounts of data, ranging from simple models like linear regression to complex ones like neural networks. 
            Important aspects include supervised learning, where models learn from labeled data, and unsupervised learning, which finds hidden patterns in unlabeled data. 
            Another key area is reinforcement learning, where systems learn by interacting with their environment to achieve the best outcomes.
            Machine learning is widely used in many fields, such as image and speech recognition, understanding natural language, medical diagnosis, self-driving cars, and personalized recommendations. 
            By analyzing large datasets, machine learning provides valuable insights and drives progress in technology and industry. Improving model accuracy and efficiency is crucial, 
            achieved through techniques like cross-validation, tuning model parameters, and regularization.
               
                
### 🔎 Overview""", unsafe_allow_html=True)


st.image(".pictures\ml.jpg")


st.markdown("""
Machine learning is essential for image classification, emotion analysis, and predictive modeling. In image classification, algorithms categorize images, such as identifying whether a room is clean or messy, by recognizing patterns in visual data. 
Emotion analysis uses machine learning to interpret text and classify emotions like happiness or sadness based on linguistic cues. Predictive modeling forecasts future outcomes, such as predicting customer churn, by analyzing historical data and identifying trends. 
Across these applications, machine learning converts raw data into valuable insights, solving complex problems in various fields.




                       
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
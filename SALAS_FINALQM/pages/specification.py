import streamlit as st

st.title("🤖 ITEQMT: APPLICATION DESCRIPTION 🖥️")


st.header('✨🌙 FEELINGS ANALYZER ✨🌙')
st.image(".pictures\feel.png")
st.image(".pictures\feel2.png")

with st.expander("Feelings Analyzer"):
    st.markdown("""
    
    #
                This app uses pre-trained machine learning models saved as pickled files to identify emotions from text inputs. 
                It's built on Streamlit, a tool for creating web apps, so users can input text and get predictions for emotions like happiness, sadness, and anger.
                This way, people can quickly understand the emotions expressed in their written content.
                
    """, unsafe_allow_html=True)

st.header('🛏️🧹IMAGE CLASSIFICATION 🛏️🧹')
st.image(".pictures\imageclassification.png")
st.image(".pictures\imageclassification1.png")

with st.expander("Image Classification of Messy vs. Clean"):
    st.markdown("""
    
    #
                This app utilizes machine learning models trained on a dataset sourced from Kaggle to classify images and determine whether a room is clean or messy. 
                The models are stored as pickled files and integrated into a Streamlit web interface for easy deployment. 
                Users can upload images of rooms through the app, which then processes the image to make a classification prediction. 
                The interface is designed to be user-friendly, allowing anyone to upload an image and quickly receive feedback on whether the room in the image is categorized as clean or messy based on the trained model's analysis.

    """, unsafe_allow_html=True)

st.header('📚👩‍💼 PREDICTOR 📚👩‍💼')
st.image(".pictures\predict.1.png")
st.image(".pictures\predict.2.png")
st.image(".pictures\predict.png")
st.image(".pictures\predict1.pngg")

with st.expander("🔍Prediction"):
    st.markdown("""
    
    This project focuses on developing a predictive model using data from Kaggle to forecast whether employees are likely to leave the company within the next two years. 
    By analyzing historical data and leveraging machine learning algorithms, the model will predict the probability of employee turnover. 
    This predictive tool aims to provide insights into future workforce dynamics, enabling strategic planning and proactive measures to enhance employee retention and organizational stability. 
    Users can upload data through a Streamlit interface, facilitating easy interaction and quick predictions based on the trained model's analysis.
                         
    """, unsafe_allow_html=True)
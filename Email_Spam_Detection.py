import streamlit as st
import pandas as pd
import joblib
import numpy as np
import seaborn as sns


st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)


model = joblib.load("Email_Spam_Detection.pkl")

subject_map = {
    "Meeting": 0,
    "Security Alert": 1,
    "Win Prize": 2,
    "Invoice": 3,
    "Offer": 4,
    "Project Update": 5,
    "Greetings": 6,
    "Account Verification": 7
}




st.markdown("<h1 class='main-title'>📧 Email Spam Detection</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Machine Learning based Spam Classifier</h3>", unsafe_allow_html=True)

st.divider()




subject = st.selectbox("Subject", list(subject_map.keys()))

email_length = st.number_input(
    "Email Length",
    min_value=1.0,
    value=100.0
)

num_links = st.number_input(
    "Number of Links",
    min_value=0,
    value=1
)

num_special_chars = st.number_input(
    "Number of Special Characters",
    min_value=0,
    value=2
)

capital_words = st.number_input(
    "Capital Words",
    min_value=0,
    value=5
)

attachment = st.selectbox(
    "Has Attachment?",
    ["No", "Yes"]
)

attachment = 1 if attachment == "Yes" else 0




if st.button("Predict", use_container_width=True):

    input_data = pd.DataFrame({
        "Subject": [subject_map[subject]],
        "Email_Length": [email_length],
        "Num_Links": [num_links],
        "Num_Special_Chars": [num_special_chars],
        "Capital_Words": [capital_words],
        "Has_Attachment": [attachment]
    })

    prediction = model.predict(input_data)[0]

    st.divider()

    if prediction == 1:
        st.error("🚨 SPAM EMAIL")
        st.markdown(
            "<p class='result' style='color:red;'>This email is likely Spam.</p>",
            unsafe_allow_html=True
        )
    else:
        st.success("✅ SAFE EMAIL")
        st.markdown(
            "<p class='result' style='color:lime;'>This email is NOT Spam.</p>",
            unsafe_allow_html=True
        )

st.divider()


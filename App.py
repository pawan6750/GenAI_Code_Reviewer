import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def review_code_google(code):
    """Uses Google Gemini API to review Python code."""
    prompt = f"""
    You are an expert Python code reviewer. Review the following code for bugs, suggest improvements, and provide a corrected version:

    ```python
    {code}
    ```
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text if response else "Error: No response from Google AI."

# Streamlit UI
st.title("GenAI - AI Code Reviewer (Google AI)")

code = st.text_area("Enter your Python code here:", height=300)

if st.button("Review Code"):
    if code.strip():
        with st.spinner("Analyzing..."):
            feedback = review_code_google(code)
        st.subheader("Review Feedback:")
        st.write(feedback)
    else:
        st.warning("Please enter some code before submitting.")

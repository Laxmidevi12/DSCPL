import streamlit as st
import os
import openai
client = openai.OpenAI(api_key=st.Secrets["OPENAI_API_KEY"])

  
st.set_page_config(page_title="DSCPL - Spiritual Chatbot", layout="centered")
st.title("🙏 DSCPL - Your Spiritual Assistant")
st.write("Welcome! How can I help you today on your spiritual journey?")

options = [
    "📖 Daily Devotion",
    "🙏 Prayer",
    "🧘 Meditation",
    "💬 Just Chat"
]
choice = st.selectbox("Choose your path:", options)

if choice:
    topic = st.text_input("What spiritual topic are you thinking about? (e.g. fear, anxiety, purpose)")

    if st.button("Start"):
        with st.spinner("Praying over your request..."):
            prompt = f"""
            You are a kind, wise Christian spiritual assistant named DSCPL.
            The user selected: {choice}.
            The topic is: {topic}.
            
            Provide encouragement with a Bible verse, a short message, and an optional prayer.
            Make it gentle and inspiring.
            """
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

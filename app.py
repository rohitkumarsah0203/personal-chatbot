import streamlit as st
import json
import os

file_path = os.path.join(os.path.dirname(__file__), "data.json")
with open(file_path, "r") as f:
    data = json.load(f)


# --- App UI ---
st.set_page_config(page_title="Rohit's Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Rohit's Personal Chatbot")
st.write("Hi! I’m Rohit’s chatbot. Ask me anything or choose an option below 👇")

# Quick buttons
options = ["About Me", "Experience", "Skills", "Projects", "Fun Fact"]
choice = st.selectbox("Pick a topic:", [""] + options)

if choice == "About Me":
    st.info(data["about"])

elif choice == "Experience":
    for exp in data["experience"]:
        st.success(f"{exp['role']} at {exp['company']} ({exp['years']})")

elif choice == "Skills":
    st.write(", ".join(data["skills"]))

elif choice == "Projects":
    for proj in data["projects"]:
        st.markdown(f"- {proj}")

elif choice == "Fun Fact":
    st.info(data["fun_facts"][0])  # You can rotate later

# Free text input
st.subheader("💬 Ask me anything")
user_input = st.text_input("Type your question here:")

if user_input:
    answer = None

    # Simple keyword matching (later can add NLP)
    if "certification" in user_input.lower():
        answer = "Currently certifications are not added, but you can update in data.json."
    elif "experience" in user_input.lower():
        answer = "I have worked at PwC as Analyst and Senior Analyst."
    elif "skill" in user_input.lower():
        answer = ", ".join(data["skills"])

    if answer:
        st.write("🤖 " + answer)
    else:
        st.write("🤖 Sorry, I don’t have data for that yet. Please check back later.")

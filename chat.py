import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(page_title="Bengisu AI", page_icon="✨")

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model_id = "models/gemini-2.5-flash" 

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("💭 Panel")
    if st.button("Sohbeti Temizle"):
        st.session_state.messages = []
        st.rerun()

st.title("✨ Sohbet Botum")

for i, message in enumerate(st.session_state.messages):
    avatar = "👩‍💻" if message["role"] == "user" else "💻"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if prompt := st.chat_input("Mesajınızı yazın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👩‍💻"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="💻"):
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=prompt,
                config={
                    "system_instruction": "Sen Bengisu'nun asistanısın. Her zaman kullanıcının yazdığı dilde cevap ver."
                }
            )
            
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.warning("Modelden boş yanıt döndü.")
                
        except Exception as e:
            st.error(f"Bağlantı Hatası: {e}")
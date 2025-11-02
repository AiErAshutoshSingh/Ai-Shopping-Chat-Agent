# app.py — Simple Mobile Shopping Chat Agent (Groq + Streamlit)
import os
import pandas as pd
import streamlit as st

# Optional: load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# Groq client import
from groq import Groq

# --- Load API key ---
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    st.error("GROQ_API_KEY not found. Put it in a .env file or set environment variable.")
    st.stop()

client = Groq(api_key=API_KEY)


@st.cache_data
def load_mobiles():
    return pd.read_csv("mobiles.csv")

mobiles = load_mobiles()

# --- Small relevance filter ---
def is_about_phones(text: str) -> bool:
    keywords = ["phone", "mobile", "camera", "battery", "ram", "storage", "screen", "under", "compare", "price"]
    t = (text or "").lower()
    return any(k in t for k in keywords)

# --- UI ---
st.set_page_config(page_title="Mobile Shopping Chat", page_icon="📱")
st.title("📱 Mobile Shopping Chat Agent ")
st.write("Ask: 'Best camera phone under ₹30000' or 'Compare OnePlus Nord 3 vs Redmi Note 12'")

if st.checkbox("Show product table"):
    st.dataframe(mobiles)

user_input = st.text_input("Type your question and press Enter:")

if user_input:
    if not is_about_phones(user_input):
        st.warning("Please ask about mobile phones (e.g., 'best phone under 30000' or 'compare models').")
    else:
        product_list = mobiles.to_dict(orient="records")
        system_message = {
            "role": "system",
            "content": (
                "You are a helpful shopping assistant specialized in mobile phones. "
                "Use only the provided product data and avoid inventing specs. "
                "Give a concise recommendation with short reasons (pros/cons)."
            )
        }
        user_message = {
            "role": "user",
            "content": (
                f"Product data: {product_list}\n\nUser question: {user_input}\n\nAnswer naturally and mention models if relevant."
            )
        }

        try:
            resp = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[system_message, user_message],
                temperature=0.6,
                max_tokens=512,
                )

            answer = resp.choices[0].message.content
        except Exception as e:
            answer = f"API error: {e}"

        st.markdown("### 💬 AI Answer")
        st.write(answer)

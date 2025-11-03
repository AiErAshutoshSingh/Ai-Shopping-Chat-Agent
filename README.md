Project Overview

This project demonstrates an AI-powered shopping chat agent designed to help users discover, compare, and purchase mobile phones through natural-language conversations.
Built as part of an AI/ML Engineer Assignment, the agent provides intelligent recommendations, feature comparisons, and product explanations — all within a simple web-based chat interface powered by Streamlit.



Goal & Scenario

The AI Shopping Agent assists users in:
💬 Answering natural language queries (e.g., “Best camera phone under ₹30,000?”).
🔍 Retrieving relevant mobiles based on user intent (budget, brand, features).
⚖️ Comparing 2–3 models with specs and trade-offs.
💡 Explaining recommendations in clear, human-like responses.
🛡️ Handling adversarial or irrelevant queries safely.
🌐 Displaying results interactively in a clean Streamlit web UI.

Architecture Overview

User Query Input → via Streamlit Chat Interface
Intent Parsing & Context Understanding → AI model interprets brand, budget, or feature needs
Data Retrieval → Fetch relevant mobiles from a mock JSON dataset
Response Generation → AI model formats recommendations & comparisons
UI Display → Streamlit dynamically displays results, product cards, and comparisons

Setup Instructions

1️⃣ Clone the Repository
git clone https://github.com/<your-username>/shopping-chat-agent.git
cd shopping-chat-agent

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Environment Variables
Create a .env file in the root directory:
GEMINI_API_KEY=your_google_ai_key_here

4️⃣ Run the Application
streamlit run app.py

Prompt Design & Safety Strategy

Prompt Design:
Context-aware system prompt defines the agent as a “mobile shopping assistant”.
Uses few-shot examples to maintain consistent tone and factual accuracy.
Prompts encourage concise, informative, and user-friendly answers.

Safety Handling:
Rejects off-topic or malicious queries (e.g., political, harmful, or unrelated topics).
Sanitizes inputs before sending to the model.
Adds response filters to ensure relevance and clarity


# Ai_Data_analyst_bot
🤖 AI Data Analysis Bot
An AI-powered bot built with LangChain, Streamlit, and Hugging Face that can:
📄 Answer questions from uploaded PDF, DOCX, or CSV files like RAG
📊 Generate charts from CSV data (e.g., bar and pie charts).
🧠 Use a lightweight T5 model (via transformers pipeline) for text generation.
🛠️ Powered by LangChain zero-shot agent with document and chart tools.

🚀 Features
File Upload Support: Upload multiple PDF, CSV, or DOCX files.
Natural Language Queries: Ask questions or request charts using plain English.
Lightweight LLM: Uses t5-base for fast, efficient performance on local machines.
Chart Generation: Create bar or pie charts from CSV columns.

.

🧠 Custom Model Support
You can replace the default t5-base model with any other model from Hugging Face that fits your use case:

python
Copy
Edit
from transformers import pipeline

# Example: Switch to t5-large, flan-t5, or any other model
llm_pipeline = pipeline("text2text-generation", model="t5-large", max_new_tokens=256)

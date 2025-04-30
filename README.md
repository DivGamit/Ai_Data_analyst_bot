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
from transformers import pipeline
Example-
llm_pipeline = pipeline("text2text-generation", model="t5-large", max_new_tokens=256)


Or use the Groq API for blazing-fast inference:
⚡ Groq API 
You can use Groq’s LPU-accelerated API for faster inference. Just modify the PipelineWrapper class to call the Groq API using requests or langchain.llms.Groq (if available). Example setup:

from langchain.llms import Groq
llm = Groq(api_key="YOUR_GROQ_API_KEY", model_name="mixtral-8x7b")
This will allow you to integrate Groq’s performance benefits into your agent pipeline.



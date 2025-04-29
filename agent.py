from langchain.agents import initialize_agent, Tool
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
from tools import qa_tool, chart_tool

# Define T5-base pipeline for text2text-generation
t5_pipeline = pipeline("text2text-generation", model="t5-base", max_new_tokens=256)

# Wrap it in LangChain's HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=t5_pipeline)

# Agent setup
tools = [
    Tool(name="QA_Tool", func=qa_tool, description="Answer questions based on uploaded documents."),
    Tool(name="Chart_Tool", func=chart_tool, description="Generate a chart from the uploaded CSV data.")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def run_agent(user_prompt, docs, dataframes):
    return agent.run({"input": user_prompt, "docs": docs, "dataframes": dataframes})

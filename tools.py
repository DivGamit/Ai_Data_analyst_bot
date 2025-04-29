from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import matplotlib.pyplot as plt
import pandas as pd

embedding_model = HuggingFaceEmbeddings()


t5_pipeline = pipeline("text2text-generation", model="t5-base", max_new_tokens=256)
llm = HuggingFacePipeline(pipeline=t5_pipeline)


def qa_tool(inputs):
    user_prompt = inputs["input"]
    docs = inputs["docs"]
    documents = [Document(page_content=doc) for doc in docs]
    db = FAISS.from_documents(documents, embedding_model)
    retriever = db.as_retriever()
    rel_docs = retriever.get_relevant_documents(user_prompt)

    chain = load_qa_chain(llm)
    return chain.run(input_documents=rel_docs, question=user_prompt)


def chart_tool(inputs):
    user_prompt = inputs["input"]
    dfs = inputs["dataframes"]
    
    if not dfs:
        return "No CSV data available."

    # Ensure we're working with a valid DataFrame (first one in the list)
    if isinstance(dfs[0], pd.DataFrame):
        df = dfs[0]
    else:
        return "No valid CSV data available."

    chart = None
    numeric_cols = df.select_dtypes(include='number').columns  # Get numeric columns

    # Split the user input into potential column names
    columns = [col.strip() for col in user_prompt.lower().split() if col.strip()]

    # If 'and', ',', 'or', or 'vs' appear, we'll treat them as separators for column names
    if 'and' in columns or ',' in columns or 'or' in columns or 'vs' in columns:
        columns = [col for col in columns if col in df.columns]

    # Handle Pie Chart request
    if "pie" in user_prompt.lower():
        if len(columns) == 1 and columns[0] in df.columns:
            col = columns[0]
            if col in numeric_cols:
                return f"Numeric columns like '{col}' cannot be used for pie charts. Please select a categorical column."
            df[col].value_counts().plot.pie(autopct='%1.1f%%')
            chart = plt.gcf()
        else:
            return "For pie charts, you must specify one column."

    # Handle Bar Chart request
    elif "bar" in user_prompt.lower() or "plot" in user_prompt.lower():
        if len(columns) >= 2:
            x_col, y_col = columns[:2]
            if x_col in df.columns and y_col in df.columns:
                if y_col not in numeric_cols:
                    return f"The column '{y_col}' must be numeric for bar charts."
                df.plot(kind='bar', x=x_col, y=y_col)
                chart = plt.gcf()
            else:
                return f"Columns {x_col} and {y_col} are not valid in the dataset."
        else:
            return "For bar charts, you must specify at least two columns."

    else:
        return "Sorry, I couldn't understand the chart request."

    return chart

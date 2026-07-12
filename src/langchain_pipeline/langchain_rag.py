from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vector_db = FAISS.load_local(
    "data/vector_db",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 5}
)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a Contract Risk Analysis Assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

Answer:
"""
)

question = input("Question: ")

documents = retriever.invoke(question)

context = "\n\n".join(
    doc.page_content
    for doc in documents
)

final_prompt = prompt.format(
    context=context,
    question=question
)

print(final_prompt)

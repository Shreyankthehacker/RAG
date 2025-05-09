from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from utils import vectorize
from llms import llm
from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough
from langchain.load import dumps, loads
from langchain_core.prompts import ChatPromptTemplate
from prompts import rag_prompt

load_dotenv()

prompt = '''You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:'''


retriever = vectorize('shreyankresume.pdf').as_retriever()

def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)


prompt = ChatPromptTemplate.from_template(rag_prompt)

rag_chain = (
    {"context":retriever |format_docs , 'question':RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


prompt = ChatPromptTemplate.from_template(rag_prompt)

generate_queries = (
    prompt
    | llm
    | StrOutputParser() 
    | (lambda x: x.split("\n"))
)


def get_unique_union(documents: list[list]):
    """ Unique union of retrieved docs """
    flattened_docs = [dumps(doc) for sublist in documents for doc in sublist]
    unique_docs = list(set(flattened_docs))
    return [loads(doc) for doc in unique_docs]


retrieval_chain = generate_queries | retriever.map() | get_unique_union




template = """Answer the following question based on this context:

{context}

Question: {question}
"""



prompt = ChatPromptTemplate.from_template(template)



final_rag_chain = (
    {"context": retrieval_chain, 
     "question": itemgetter("question")} 
    | prompt
    | llm
    | StrOutputParser()
)


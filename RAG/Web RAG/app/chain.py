from langchain_exa import ExaSearchRetriever
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv; load_dotenv()

retriever = ExaSearchRetriever(k=3, highlights=True)

document_prompt = PromptTemplate.from_template("""
<source>                                        
    <url>{url}</url>
    <highlights>{highlights}</highlights>
</source>
""")

document_chain = RunnableLambda(
    lambda document: {
        "highlights": document.metadata["highlights"], 
        "url": document.metadata["url"]
    }
) | document_prompt

retrieval_chain = retriever | document_chain.map() | (lambda docs: "\n".join([i.text for i in docs]))   # .map() is a langchain function that invokes a chain one element at a time

Query_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research assistant. You use xml-formatted context to research people's questions."),
    ("human", """
Please answer the following query based on the provided context. Please cite your sources at the end of your response.:
     
Query: {query}
--------------------
<context>
{retriver}
</context>
""")
])

llm = ChatOpenAI(temperature=0.2)

Main_chain = (RunnableParallel({
    "retriver": retrieval_chain,        # so here we the chain looks at the first input type and uses it as the input of our agent so if we place query first since it is a 
    "query" : RunnablePassthrough(),    # Runnable passthrought it could be any type it needs to the model kinda freezez and doesnt know which type to expect so either we stick with retreiver befrore since tin that chain the first imput is the input of retriever (str) or we need to specify it by saying at the end of the chain """.with_types(input_type=str)"""
})| Query_prompt | llm).with_types(input_type=str)      # which isnt neccacary now just to remember it
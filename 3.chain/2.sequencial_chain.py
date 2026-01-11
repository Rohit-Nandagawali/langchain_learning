from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

prompt1= PromptTemplate(template="Generate a detailed report on the topic: {topic}.",
                        input_variables=["topic"])

prompt2= PromptTemplate(template="Summarize the following report in 5 points: {report}.",input_variables=["report"])

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser() 
chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "Unemployment in India"})

chain.get_graph().print_ascii

print(result)
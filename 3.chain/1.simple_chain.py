from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interasting facts about {topic}.",
                        input_variables=["topic"]
                        )

model = init_chat_model("groq:llama-3.1-8b-instant")

parser = StrOutputParser() # directly returns string output, no need responce.content

chain = prompt | model | parser

result = chain.invoke({"topic": "Agentic AI"})
print(result)




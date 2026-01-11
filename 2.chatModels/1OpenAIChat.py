from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model="Gemma-3-27B-ArliAI-RPMax-v3",
    openai_api_base="https://api.arliai.com/v1",
                   )

result = model.invoke("What is the capital of India?")
print(result.content)

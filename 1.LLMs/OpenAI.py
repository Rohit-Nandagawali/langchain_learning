from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

model = OpenAI(model="Gemma-3-27B-ArliAI-RPMax-v3",
    openai_api_base="https://api.arliai.com/v1")

result = model.invoke("What is the capital of India?")
print(result)
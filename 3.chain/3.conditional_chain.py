from typing import Literal
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import Literal


load_dotenv()


class SentimentResponse(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field( description="The sentiment classification of the feedback"
    )

parser = StrOutputParser()


parser2 = PydanticOutputParser(pydantic_object=SentimentResponse)


prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback as Positive Negative {feedback}. \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)



model =  ChatGroq(model="llama-3.1-8b-instant")

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="Write an appropriate responce for this positive feedback: {feedback}.",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate responce for this negative feedback: {feedback}.",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch( 
    (lambda x: x.sentiment=="Positive",prompt2 | model | parser), #(condition, chain) if this condition is met, run this chain
     (lambda x: x.sentiment=="Negative",prompt3 | model | parser),
   RunnableLambda(lambda x: "Unable to classify sentiment.") #default case

)

chain = classifier_chain | branch_chain

res = chain.invoke({"feedback": "The product quality is excellent and I am very satisfied with my purchase."})

print(res)


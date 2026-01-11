from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()
# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

print(multiply.invoke({'a':3, 'b':4}))  #12


# tool binding
llm = ChatGroq(model="llama-3.1-8b-instant")
llm_with_tools = llm.bind_tools([multiply])

# llm_with_tools.invoke('can you multiply 3 with 1000').tool_calls[0]
# AIMessage(.... tool_calls=[{'name': 'multiply', 'args': {'a': 3, 'b': 1000}, 'id': '0fpzkrac4', 'type': 'tool_call'}], usage_metadata={'input_tokens': 239, 'output_tokens': 20, 'total_tokens': 259})

query = HumanMessage('can you multiply 3 with 1000')

messages = [query]

messages

result = llm_with_tools.invoke(messages)

messages.append(result)

messages

tool_result = multiply.invoke(result.tool_calls[0])

tool_result

messages.append(tool_result)

messages

llm_with_tools.invoke(messages).content
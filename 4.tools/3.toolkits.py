from langchain_community.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result."""
    return a * b

class MathToolkit:
    """A toolkit for basic math operations."""

    def get_tools(self):
        return [add_numbers, multiply_numbers]
    

math_toolkit = MathToolkit()
tools = math_toolkit.get_tools()

for t in tools:
    print(f"Tool Name: {t.name}, Description: {t.description}")

from langchain_community.tools import tool

@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result."""
    return a * b

result = multiply_numbers.invoke({"a": 6, "b": 7})
print(f"The result of multiplication is: {result}")
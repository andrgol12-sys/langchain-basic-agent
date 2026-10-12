from langchain_core.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """Умножает два целых числа и возвращает результат."""
    return a * b
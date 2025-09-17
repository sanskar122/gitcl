"""
tesst.py

A simple demo module to show a greeting function.
"""

def say_hello(name: str = "dear") -> str:
    """
    Return a personalized greeting message.

    Args:
        name (str): The name of the person to greet. Defaults to "dear".

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(say_hello())
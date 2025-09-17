def say_hello(name: str = "dear") -> str:
    """
    Return a personalized greeting message.

    Args:
        name (str): The name of the person to greet. Defaults to "dear".

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


# Example usage
print(say_hello())          # Hello, dear!
print(say_hello("Sanskar")) # Hello, Sanskar!
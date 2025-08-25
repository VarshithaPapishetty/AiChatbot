import re

def calculate(query: str):
    """
    Simple calculator tool that handles addition and multiplication.
    Supports phrases like 'add 2 and 3', 'multiply 5 and 6', etc.
    """
    query = query.lower()

    # Match addition
    add_match = re.findall(r"(\d+)", query) if "add" in query or "plus" in query or "sum" in query else None
    if add_match and len(add_match) >= 2:
        return int(add_match[0]) + int(add_match[1])

    # Match multiplication
    mult_match = re.findall(r"(\d+)", query) if "multiply" in query or "times" in query or "x" in query or "*" in query else None
    if mult_match and len(mult_match) >= 2:
        return int(mult_match[0]) * int(mult_match[1])

    return "Sorry, I can only do addition and multiplication right now."

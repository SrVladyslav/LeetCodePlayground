"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false
"""


def valid_parentheses(s: str) -> bool:
    if not (1 <= len(s) <= 10**4):
        return False

    options: dict[str, str] = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    stack: list[str] = []

    for a in s:
        found_closing = options.get(a)

        if found_closing is None:  # We found opening actually
            stack.append(a)

        elif stack:  # Now it should be an actual closing
            val = stack.pop()
            if (
                val != found_closing
            ):  # Means that the last opening for the current closing are different
                return False
        else:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    print(f"Valid parentheses for (): {valid_parentheses('()')}")
    print(f"Valid parentheses for ()[]: {valid_parentheses('()[]')}")
    print(f"Valid parentheses for ()[][]: {valid_parentheses('()[][]')}")
    print(f"Valid parentheses for ([)]: {valid_parentheses('([)]')}")
    print(f"Valid parentheses for ]: {valid_parentheses(']')}")

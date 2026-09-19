"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


def longest_valid_parentheses(s: str) -> int:
    if not (0 <= len(s) <= 3 * 10**4):
        return 0

    max_length: int = 0
    # -1 is an artifical value to start the stack idx
    stack: list[int] = [
        -1
    ]  # We will be usiong the string indexes to store the last valid number

    for idx, char in enumerate(s):
        if char == "(":  # just add the string to stack
            stack.append(idx)

        else:  # char ")"
            # We should pop the parenthesis if exists
            if stack:
                stack.pop()
                # Now we should update the max length  if we can
                max_length = max(max_length, idx - (stack[-1] if stack else 0))

            else:
                # In case we have no stack, we reset the counting by appending the current index
                stack.append(idx)

    return max_length


if __name__ == "__main__":
    print(f"Longest valid parentheses for '': {longest_valid_parentheses('')}")  # 0
    print(f"Longest valid parentheses for (): {longest_valid_parentheses('()')}")  # 2
    print(
        f"Longest valid parentheses for ()((): {longest_valid_parentheses('()(()')}"
    )  # 2
    print(
        f"Longest valid parentheses for )()()): {longest_valid_parentheses(')()())')}"
    )  # 4

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

input = 3[a2[c]]3[abc]
output = accaccaccabcabcabc

a[]b, 0[abc]


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


def decode_string(string: str) -> str:
    if not (1 <= len(string) <= 30):
        return ""

    # The best appraoch here is the stack
    stack: list[tuple[str, int]] = []
    processed: str = ""  # Processed string and tmp
    repetitions: int = 0  # Stores the current number of repetitions

    for char in string:
        if char.isdigit():
            repetitions = repetitions * 10 + int(char)

        elif char == "[":
            # Save the current processed data with the repetitions so we can process the inner one
            stack.append((processed, repetitions))
            # Reset the tmp values isnce they are in stack
            processed = ""
            repetitions = 0
        elif char == "]":
            # We are at the end of one sub problem, so just get the data, apply repetitions and add it to the parent problem
            previous, reps = stack.pop()
            processed = (
                previous + processed * reps
            )  # Can be used in the parent problem if we have ]]
        else:
            processed += char

    return processed


if __name__ == "__main__":
    print(f"Decoded string for 3[a2[c]]: {decode_string('3[a2[c]]')}")
    print(f"Decoded string for 2[abc]3[cd]ef: {decode_string('2[abc]3[cd]ef')}")
    print(f"Decoded string for 3[a]2[bc]: {decode_string('3[a]2[bc]')}")
    print(f"Decoded string for 3[a2[c]]3[abc]: {decode_string('3[a2[c]]3[abc]')}")
    print(f"Decoded string for a[]b: {decode_string('a[]b')}")
    print(f"Decoded string for 0[abc]: {decode_string('0[abc]')}")

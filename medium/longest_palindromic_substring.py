"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def longest_palindromic_substring(s: str) -> str:
    if not (1 <= len(s) <= 1000):
        return ""

    start: int = 0
    max_length: int = 0

    def expand(left_ptr: int, right_ptr: int) -> None:
        nonlocal start, max_length

        while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
            current_length = right_ptr - left_ptr + 1
            if current_length > max_length:
                max_length = current_length
                start = left_ptr

            left_ptr -= 1
            right_ptr += 1

    # Run over the full array and try to get to expand in order to get the info
    for i in range(len(s)):
        # Explore the odd palindrome cases
        expand(i, i)
        # explore the even palindromes
        expand(i, i + 1)

    return s[start : start + max_length]


if __name__ == "__main__":
    print(f"LPS for babad: {longest_palindromic_substring('babad')}")
    print(f"LPS for cbbd: {longest_palindromic_substring('cbbd')}")

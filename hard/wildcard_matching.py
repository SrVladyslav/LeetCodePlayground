"""
44. Wildcard Matching
Solved
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        string_ptr, pattern_ptr = 0, 0
        last_pattern_ptr = -1
        last_string_ptr = -1

        while string_ptr < len(s):
            if pattern_ptr < len(p) and (
                s[string_ptr] == p[pattern_ptr] or p[pattern_ptr] == "?"
            ):
                string_ptr += 1
                pattern_ptr += 1

            # Process *
            elif pattern_ptr < len(p) and p[pattern_ptr] == "*":
                last_pattern_ptr = pattern_ptr
                last_string_ptr = string_ptr
                pattern_ptr += (
                    1  # Advance the pattern pointer just to check the next stuff
                )

            # Mismatch in the check, but we still haver theprevious * wildcard
            elif last_pattern_ptr != -1:
                pattern_ptr = (
                    last_pattern_ptr + 1
                )  # We don't advance the prev pattern pointer
                last_string_ptr += (
                    1  # We advance the string last pointer for the wildcard
                )
                string_ptr = last_string_ptr
            # Final mismatch, with no wildcard
            else:
                return False

        # Remaining pattern myust contain only *
        while pattern_ptr < len(p) and p[pattern_ptr] == "*":
            pattern_ptr += 1

        return pattern_ptr == len(p)

    def isMatchDP(self, s: str, p: str) -> bool:
        rows = len(p)
        cols = len(s)

        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        # Base case
        dp[0][0] = True

        for row in range(1, rows + 1):
            if p[row - 1] == "*":
                dp[row][0] = dp[row - 1][0]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                # Case normal letter or ?
                if p[row - 1] == s[col - 1] or p[row - 1] == "?":
                    dp[row][col] = dp[row - 1][col - 1]

                # Case "*"
                # -> Take the letter
                # -> Skip the letter
                elif p[row - 1] == "*":
                    # * consumes >= 1, * consumes 0
                    dp[row][col] = dp[row][col - 1] or dp[row - 1][col]

        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("aa", "a"))
    print(solution.isMatch("aa", "*"))
    print(solution.isMatch("cb", "?a"))
    print(solution.isMatch("aab", "*b"))
    print(solution.isMatchDP("aab", "*b"))

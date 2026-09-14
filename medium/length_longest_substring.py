def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0 or len(s) > 10**5:
        return 0

    max_length: int = 0
    substrings: dict[str, bool] = {}

    fast, slow = 0, 0

    while fast < len(s):
        curr_char = s[fast]

        while substrings.get(curr_char, False):
            substrings[s[slow]] = False
            slow += 1

        substrings[curr_char] = True
        max_length = max(max_length, fast - slow + 1)
        fast += 1

    return max_length


def lengthOfLongestSubstringOptimized(self, s: str) -> int:
    if len(s) == 0 or len(s) > 10**5:
        return 0

    max_length: int = 0
    substrings: set[str] = set()
    slow: int = 0

    for fast, char in enumerate(s):
        # Test for the known substring
        while char in substrings:
            substrings.remove(s[slow])
            slow += 1

        max_length = max(max_length, fast - slow + 1)
        substrings.add(char)

    return max_length

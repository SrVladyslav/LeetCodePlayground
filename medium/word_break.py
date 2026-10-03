class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp: dict[int, bool] = {}

        dp1: list[bool] = [False] * (length + 1)
        dp1[length] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : (i + len(word))] == word:
                    dp1[i] = dp1[i + len(word)]
                    if dp1[i]:
                        break

        return dp1[0]

        def backtrack(index: int) -> bool:
            if index == length:
                return True

            if index in dp:
                return dp[index]

            dp[index] = False
            for word in wordDict:
                if not s[index:].startswith(word):
                    continue

                print(f"[{index}]: {word} -> {s[(index+len(word)):]}")
                dp[index] = dp[index] or backtrack(index + len(word))

            return dp[index]

        return backtrack(0)

"""
Daily Temperatures
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    # Monotonic stack wey
    result: list[int] = [0] * len(temperatures)
    monotonic_stack: list[(int, int)] = []  # Temp and index

    for i in range(len(temperatures) - 1, -1, -1):
        # since we need strictly warmer, we ned to delete the equal ones.
        while monotonic_stack and temperatures[i] >= monotonic_stack[-1][0]:
            monotonic_stack.pop()

        if not monotonic_stack:  # Meaning that we don't have a comparison, so 0
            result[i] = 0
        else:
            result[i] = monotonic_stack[-1][1] - i

        # Always push the less that the top value on the stack
        monotonic_stack.append((temperatures[i], i))

    return result


if __name__ == "__main__":
    print(
        f"Daily temperatures for [30,38,30,36,35,40,28]: {daily_temperatures([30,38,30,36,35,40,28])}"
    )
    print(f"Daily temperatures for [22,21,20]: {daily_temperatures([22,21,20])}")

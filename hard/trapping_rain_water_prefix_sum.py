"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

"""


def trap(height: list[int]) -> int:
    if not height:
        return 0

    # Approach with DP
    prefix_max: list[int] = [0] * len(height)
    prefix_max[0] = height[0]
    suffix_max: list[int] = [0] * len(height)
    suffix_max[-1] = height[-1]
    for i in range(1, len(height)):
        prefix_max[i] = max(prefix_max[i - 1], height[i])

    for i in range(len(height) - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], height[i])
    result: int = 0
    for i, h in enumerate(height):
        result += min(prefix_max[i], suffix_max[i]) - h

    return result


def trap_pointers(height: list[int]) -> int:
    max_left: int = 0
    max_right: int = 0
    left: int = 0
    right: int = len(height) - 1

    water: int = 0

    while left < right:
        if height[left] <= height[right]:
            max_left = max(max_left, height[left])
            water += max_left - height[left]
            left += 1
        else:
            max_right = max(max_right, height[right])
            water += max_right - height[right]
            right -= 1

    return water


def trap_monotonick_decreasing_stack(height: list[int]) -> int:
    stack: list[int] = []

    water: int = 0

    # Monotonic decreasing stack  x
    for i, curr_value in enumerate(height):
        while stack and height[stack[-1]] < curr_value:
            top = stack.pop()

            if not stack:
                break  # No stack at all

            left = stack[-1]

            width = i - left - 1

            bounded_height = min(curr_value, height[left]) - height[top]

            water += width * bounded_height

        stack.append(i)

    return water


if __name__ == "__main__":
    print(f"For [0,1,0,2,1,0,1,3,2,1,2,1] is: {trap([0,1,0,2,1,0,1,3,2,1,2,1])}")  # 6
    print(f"For [4,2,0,3,2,5] is : {trap([4,2,0,3,2,5])}")  # 9

    print(
        f"\nFor [0,1,0,2,1,0,1,3,2,1,2,1] is: {trap_pointers([0,1,0,2,1,0,1,3,2,1,2,1])}"
    )  # 6
    print(f"For [4,2,0,3,2,5] is : {trap_pointers([4,2,0,3,2,5])}")  # 9
    print(
        f"\nFor [0,1,0,2,1,0,1,3,2,1,2,1] is: {trap_monotonick_decreasing_stack([0,1,0,2,1,0,1,3,2,1,2,1])}"
    )  # 6
    print(
        f"For [4,2,0,3,2,5] is : {trap_monotonick_decreasing_stack([4,2,0,3,2,5])}"
    )  # 9

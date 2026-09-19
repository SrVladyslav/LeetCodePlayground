"""
Largest Rectangle In Histogram
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Input: heights = [7,1,7,2,2,4]
Output: 8

Input: heights = [1,3,7]
Output: 7

"""


def largest_rectangle_area(heights: list[int]) -> int:
    monotonic_stack: list[tuple[int, int]] = []  # (index, height)
    max_area: int = 0

    for idx, curr_height in enumerate(heights):
        # Create the stack
        start: int = idx  # We don't know if we can extend this backwards or not

        # Should be increasing monotonic stack, since we want the maximum
        while monotonic_stack and curr_height < monotonic_stack[-1][1]:
            index, height = monotonic_stack.pop()
            # Process the height bar size
            max_area = max(max_area, height * (idx - index))
            # We update the index to the last equal one on the left, basically extend it to the left
            start = index

        # Push the current max number to the stack
        monotonic_stack.append((start, curr_height))

    # Process all the other parts from the stack , which are extendable towards the end of the stack
    while monotonic_stack:
        top_idx, top_value = monotonic_stack.pop()
        max_area = max(max_area, top_value * (len(heights) - top_idx))

    return max_area


if __name__ == "__main__":
    print(f"Max area for [7,1,7,2,2,4]: {largest_rectangle_area([7,1,7,2,2,4])}")
    print(f"Max area for [1,3,7]: {largest_rectangle_area([1,3,7])}")

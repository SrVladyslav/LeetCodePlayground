def container_with_most_water(height: list[int]) -> int:
    length = len(height)

    if not (2 <= length <= 10**5):
        return 0

    ptr_left: int = 0
    ptr_right: int = length - 1
    max_area: int = 0  # Max container area overall

    while ptr_left < ptr_right:
        # Current area: min(verticals) * base
        curr_area: int = min(height[ptr_left], height[ptr_right]) * (
            ptr_right - ptr_left
        )

        max_area = max(max_area, curr_area)

        # Move the lowest pointer
        if height[ptr_left] < height[ptr_right]:
            ptr_left += 1
        else:
            ptr_right -= 1

    return max_area


def container_with_most_water_improved(height: list[int]) -> dict[str, int]:
    length = len(height)

    if not (2 <= length <= 10**5):
        return {"max_area": 0, "start": -1, "end": -1}

    ptr_left: int = 0
    ptr_right: int = length - 1
    max_area: int = 0  # Max container area overall
    start = end = -1

    while ptr_left < ptr_right:
        # Current area: min(verticals) * base
        curr_area: int = min(height[ptr_left], height[ptr_right]) * (
            ptr_right - ptr_left
        )

        if curr_area > max_area:
            max_area = curr_area
            start = ptr_left
            end = ptr_right

        # Move the lowest pointer
        if height[ptr_left] < height[ptr_right]:
            ptr_left += 1
        else:
            ptr_right -= 1

    return {"max_area": max_area, "start": start, "end": end}


if __name__ == "__main__":
    print(
        f"Max area for [1,8,6,2,5,4,8,3,7]: {container_with_most_water([1,8,6,2,5,4,8,3,7])}"
    )
    print(f"Max area for [1,2]: {container_with_most_water([1,2])}")
    print(f"Max area for []: {container_with_most_water([])}")
    print("\n\n")
    print(
        f"Max area for [1,8,6,2,5,4,8,3,7]: {container_with_most_water_improved([1,8,6,2,5,4,8,3,7])}"
    )
    print(f"Max area for [1,2]: {container_with_most_water_improved([1,2])}")
    print(f"Max area for []: {container_with_most_water_improved([])}")

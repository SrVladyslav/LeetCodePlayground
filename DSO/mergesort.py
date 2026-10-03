def mergesort(nums: list[int]) -> list[int]:
    if not nums:
        return []

    def merge(a: list[int], b: list[int]) -> list[int]:
        ptr1 = 0
        ptr2 = 0
        new_list = []
        while ptr1 < len(a) or ptr2 < len(b):
            if ptr2 >= len(b) or (ptr1 < len(a) and a[ptr1] < b[ptr2]):
                new_list.append(a[ptr1])
                ptr1 += 1
            else:
                new_list.append(b[ptr2])
                ptr2 += 1
        return new_list

    def divide(nums: list[int], left: int, right: int) -> list[int]:
        if right - left <= 1:
            return nums[left:right]

        mid = left + (right - left) // 2
        left_list = divide(nums, left, mid)
        right_list = divide(nums, mid, right)
        return merge(left_list, right_list)

    return divide(nums, 0, len(nums))


if __name__ == "__main__":
    array = [0, 0, 2, 1, 2, 1, 1, 0, 2]
    print(f"Result for {array}: {mergesort(array)}")

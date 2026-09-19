# USING THE PREFIX X SUFFIX SM
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    output = [1] * n

    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output


if __name__ == "__main__":
    print(
        f"Product of array except self for [1,2,4,6]: {product_except_self([1,2,4,6])}"
    )  # [48,24,12,8]
    print(
        f"Product of array except self for [-1,0,1,2,3]: {product_except_self([-1,0,1,2,3])}"
    )  # [0,-6,0,0,0]

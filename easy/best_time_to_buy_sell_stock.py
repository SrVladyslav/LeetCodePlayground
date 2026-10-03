def max_profit(prices: list[int]) -> int:
    # Monotonick stack
    stack: list[int] = []  # (curr_i, min_i)
    top_profit: int = 0
    min_price: int = prices[0]

    # Increasing stack
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            stack.pop()

        top_profit = max(top_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
        stack.append(i)

    return top_profit


if __name__ == "__main__":
    print(f"Max profit for [5,1,5,6,7,1,10]: {max_profit([5,1,5,6,7,1,10])}")  # 9
    print(f"Max profit for [3,4,1]: {max_profit([3,4,1])}")  # 1
    print(f"Max profit for [7,1,5,3,6,4]: {max_profit([7,1,5,3,6,4])}")  # 5
    print(f"Max profit for [10,8,7,5,2]: {max_profit([10,8,7,5,2])}")  # 0

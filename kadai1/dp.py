def knapsack(items, weights, W):
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + weights[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(items[i - 1])
            w -= weights[i - 1]

    return result

# テストコード
# def test_knapsack():
#     items = [1, 2, 3, 4, 5]
#     weights = [3, 4, 5, 6, 7]
#     W = 10
#     expected_result = [5, 1]
#     assert knapsack(items, weights, W) == expected_result

#     items = [1, 2, 3, 4, 5]
#     weights = [2, 3, 4, 5, 9]
#     W = 15
#     expected_result = [5, 4, 2, 1]
#     assert knapsack(items, weights, W) == expected_result

#     print("All tests passed.")

if __name__ == "__main__":
    items = [1, 2, 3]
    weights = [10, 20, 30]
    W = 50
    print(knapsack(items, weights, W))

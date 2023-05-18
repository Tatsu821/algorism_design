from itertools import combinations

def knapsack_bruteforce(items, weights, W):
    max_weight = 0
    result = []

    for i in range(1, len(items) + 1):
        for subset in combinations(zip(items, weights), i):
            subset_items, subset_weights = zip(*subset)
            total_weight = sum(subset_weights)
            if total_weight <= W and total_weight > max_weight:
                max_weight = total_weight
                result = list(subset_items)

    return result, max_weight

# テストコード
def test_knapsack_bruteforce():
    items = [1, 2, 3, 4, 5]
    weights = [3, 4, 5, 6, 7]
    W = 10
    expected_result = [1, 5]
    print(knapsack_bruteforce(items, weights, W)[0])
    print(knapsack_bruteforce(items, weights, W)[1])
    assert knapsack_bruteforce(items, weights, W)[0] == expected_result

    items = [1, 2, 3, 4, 5]
    weights = [2, 3, 4, 5, 9]
    W = 20
    expected_result = [1, 3, 4, 5]
    print(knapsack_bruteforce(items, weights, W)[0])
    print(knapsack_bruteforce(items, weights, W)[1])
    assert knapsack_bruteforce(items, weights, W)[0] == expected_result

    print("All tests passed.")

if __name__ == "__main__":
    test_knapsack_bruteforce()

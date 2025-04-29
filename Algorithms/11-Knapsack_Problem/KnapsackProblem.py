def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n+1)]

    # Build the table dp[][] in bottom-up manner
    for i in range(1, n + 1):  # Start i from 1, as we are using 1-based indexing for items
        for w in range(1 , capacity + 1):  # Start w from 1 for capacities
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Example usage
if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7

    max_value = knapsack(weights, values, capacity)
    print(f"The maximum value that can be put in the knapsack is: {max_value}")

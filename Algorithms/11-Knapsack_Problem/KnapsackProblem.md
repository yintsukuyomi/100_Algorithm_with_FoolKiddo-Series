## ✅ What is the Knapsack Problem?

### The Knapsack Problem is a **combinatorial optimization problem** where you must choose a subset of items to maximize the total value without exceeding a weight limit.

The problem is called **"Knapsack"** because it is analogous to filling a **knapsack** with items that have both weight and value, subject to a maximum weight capacity.

---

### 📊 Time & Space Complexity

- **Time Complexity (0/1 Knapsack):** O(n * W)  
  *(n = number of items, W = maximum weight capacity)*
- **Space Complexity:** O(n * W)  
  *(due to the DP table used for storing intermediate results)*

---

## 🧠 Algorithm Steps:

1. Create a **2D array** `dp` where `dp[i][w]` represents the maximum value achievable with the first `i` items and a weight limit `w`.
2. Initialize the first row and column of the array with zeros (no value when there are no items or weight limit is zero).
3. For each item `i` (from 1 to n):
   - For each weight `w` (from 1 to W):
     - If the item `i` **does not fit** in the knapsack (i.e., `weight[i] > w`), then `dp[i][w] = dp[i-1][w]`.
     - Otherwise, choose the maximum of:  
       - Not including the item: `dp[i-1][w]`,  
       - Including the item: `dp[i-1][w-weight[i]] + value[i]`.
4. The final value `dp[n][W]` will give the maximum value that can be obtained without exceeding the weight limit.

---

## ✅ Real-Life Analogy: *"Packing for a Trip with Limited Luggage Space"*

Imagine you're going on a trip and you're trying to **pack your suitcase**. You have several items, each with a **weight** and **value** (for example, clothes, gadgets, etc.), but your luggage has a **weight limit**.

---

### 🔁 How would you do it manually?

1. You look at all the items you want to pack.
2. You start deciding which **items to include** based on their importance (value) and how much **weight** they add to your luggage.
3. You can either pack an item or leave it out, but you want to make sure you get the **most valuable items** without exceeding the weight limit.
4. At the end, your suitcase will have the **optimal set of items** that gives you the **maximum value** within the allowed weight limit.

---

This is the essence of the **Knapsack Problem** —  
**maximize the value** of the items you can carry while staying within the **weight limit**.

## ✅ What is Floyd-Warshall Algorithm?

### Floyd-Warshall is a **dynamic programming** algorithm used to find the **shortest paths between all pairs of nodes** in a weighted graph.

It can handle **positive and negative edge weights**, but **not negative cycles**.

---

### 📊 Time & Space Complexity

- **Time Complexity:** O(V³)  
- **Space Complexity:** O(V²)  
  *(V = number of vertices)*

---

## 🧠 Algorithm Steps:

1. Create a **distance matrix** where `dist[i][j]` is the weight of the edge from node `i` to node `j`.  
   If no direct edge exists, set it to infinity.
2. Set `dist[i][i] = 0` for all `i` (distance to self is zero).
3. For each node `k` from 1 to V:  
   - For each node `i`:  
     - For each node `j`:  
       - Update `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
4. After all iterations, `dist[i][j]` will hold the **shortest distance** from `i` to `j`.

---

## ✅ Real-Life Analogy: *"Choosing the Best Travel Route Between Cities"*

Imagine a **network of cities**, connected by **flights with different costs**.  
Your goal is to find the **cheapest cost** to travel between **every pair of cities**.

---

### 🔁 How would you do it manually?

1. You start by **listing all direct flight prices** between every city.
2. Then, you ask: “If I pass through **another city**, would it be cheaper?”
3. For every pair of cities `(A, B)`, you consider **each city C as an intermediate stop**.
4. If going from `A → C → B` is **cheaper than direct A → B**, you update your route.
5. You do this for **every possible route combination** and update the best known costs.

---

This is exactly what **Floyd-Warshall** does —  
It **systematically improves all-pairs paths** using **intermediate nodes**.

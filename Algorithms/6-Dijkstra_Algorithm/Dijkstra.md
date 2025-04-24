## ✅ What is Dijkstra’s Algorithm?

### Dijkstra’s Algorithm is a **greedy** algorithm used to find the **shortest path** from a **starting node** to all other nodes in a **weighted graph** with non-negative edge weights.

It is widely used in routing, navigation systems, and network optimization.

---

### 📊 Time & Space Complexity

- **Time Complexity:**
  - Using **Min-Heap (Priority Queue):** O((V + E) log V)
  - Using **Simple Array:** O(V²)
- **Space Complexity:** O(V) *(for distance and visited arrays)*

---

## 🧠 Algorithm Steps:

1. Assign **infinity** as the initial distance to all nodes except the **source**, which is set to 0.
2. Mark all nodes as **unvisited**. Create a **priority queue** and insert the source node.
3. While the queue is not empty:
   - Select the node with the **minimum distance**.
   - For each unvisited neighbor, **calculate tentative distances** via the current node.
   - If this new distance is **smaller**, update it.
4. Mark the current node as **visited**.
5. Repeat until all nodes have been visited or the shortest path is found.

---

## 🧭 Real-Life Analogy: *"Finding the Fastest Route in a City Map"*

Imagine you're using a GPS to navigate a city. You want to find the **fastest route** from your **home** to every other location in the city.

---

### 🔁 How would you do it manually?

1. Start at your **home** — the known location (distance 0).
2. Look at all **roads** leading out and calculate the **time** to reach nearby places.
3. Choose the **closest unvisited location** and mark it as visited.
4. From this new location, again calculate the time to reach its neighbors.
5. If you find a **faster route** to a place you already considered, **update** it.
6. Keep expanding outward, always choosing the **nearest unvisited location**.
7. Eventually, you'll know the **shortest travel time** to every place in the city.

---

This is the core idea of **Dijkstra’s Algorithm** —  
**expand outward**, always choosing the **closest** path first, and **never re-visiting** a location unnecessarily.

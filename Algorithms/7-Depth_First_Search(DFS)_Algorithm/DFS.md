## ✅ What is Depth-First Search (DFS)?

### Depth-First Search (DFS) is a **graph traversal algorithm** that explores as far as possible along each branch before **backtracking**.

It is used to systematically explore all the vertices and edges of a graph or a tree.

---

### 📊 Time & Space Complexity

- **Time Complexity:** O(V + E)  
  *(V = number of vertices, E = number of edges)*
- **Space Complexity:** O(V)  
  *(due to recursion stack or explicit stack usage)*

---

## 🧠 Algorithm Steps:

1. Start from a **source node** (vertex).
2. **Visit** the current node and **mark** it as visited.
3. Recursively (or using a stack) **explore each unvisited neighbor**.
4. If a neighbor has already been visited, **backtrack**.
5. Continue until **all reachable nodes** have been visited.

---

## ✅ Real-Life Analogy: *"Exploring Rooms in a Maze"*

Imagine you're inside a huge **maze** with multiple **rooms** connected by **doors**.  
You want to **visit every room** at least once.

---

### 🔁 How would you do it manually?

1. Start at the **entrance room**.
2. Choose a **door** and **walk** through it to the next room.
3. From the new room, **keep going deeper** through the first available unexplored door.
4. If you enter a room where **no new doors** are available (dead-end), **backtrack** to the last room that had unexplored doors.
5. Repeat the process until **all rooms** have been visited.

---

This is the spirit of **DFS** —  
**go as deep as you can first**, and only **backtrack** when necessary to find unexplored paths.

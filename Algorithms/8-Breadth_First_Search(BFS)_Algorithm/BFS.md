## ✅ What is Breadth-First Search (BFS)?

### Breadth-First Search (BFS) is a **graph traversal algorithm** that explores all the neighbors of a node **before moving to the next level**.

It systematically visits nodes layer by layer, starting from a selected source node.

---

### 📊 Time & Space Complexity

- **Time Complexity:** O(V + E)  
  *(V = number of vertices, E = number of edges)*
- **Space Complexity:** O(V)  
  *(due to the queue used for traversal)*

---

## 🧠 Algorithm Steps:

1. Start from a **source node** (vertex).
2. **Visit** the node and **mark** it as visited.
3. **Enqueue** all **unvisited neighbors** into a **queue**.
4. **Dequeue** the next node and **repeat** the process.
5. Continue until the **queue becomes empty**, meaning all reachable nodes have been visited.

---

## ✅ Real-Life Analogy: *"Spreading a Rumor at a Party"*

Imagine you're at a **big party** with lots of **people** (nodes), and you want to **spread a rumor** to everyone as quickly as possible.

---

### 🔁 How would you do it manually?

1. You **tell the rumor** to all the people **standing closest** to you.
2. Each of those people, **at the same time**, tells the rumor to all **their immediate neighbors**.
3. Then, the next wave of people spreads the rumor to their neighbors, and so on.
4. The information spreads **level by level** — first your direct contacts, then their contacts, then their contacts' contacts, and so forth.

---

This is the heart of **BFS** —  
**explore everything close first**, then **move outward step by step**.

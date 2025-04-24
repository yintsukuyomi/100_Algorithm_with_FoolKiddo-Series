## ✅ What is Merge Sort?

### Merge Sort is an efficient, general-purpose, comparison-based **divide and conquer** sorting algorithm.

It works by **dividing** the array into smaller subarrays, **sorting** each of them recursively, and then **merging** the sorted subarrays to produce the final sorted array.

---

### 📊 Time & Space Complexity

- **Worst Case:** O(n log n)  
- **Best Case:** O(n log n)  
- **Average Case:** O(n log n)  
- **Space Complexity:** O(n) *(requires additional space for merging)*

---

## 🧠 Algorithm Steps:

1. If the array has **0 or 1 elements**, it's already sorted — return it.
2. **Divide** the array into two halves.
3. **Recursively sort** each half.
4. **Merge** the two sorted halves into a single sorted array.
5. Repeat the process until the entire array is sorted.

---

## 🧩 Real-Life Analogy: *"Organizing Tournament Brackets"*

Imagine you’re organizing a **chess tournament** where you want to rank players from **strongest to weakest**, but you can't compare everyone at once.

---

### 🔁 How would you do it manually?

1. Split all players into **pairs** and have each pair play a match.
2. Record the winners and move them to the next round.
3. Keep dividing and matching winners until each group is **sorted by strength**.
4. Then, **merge** these small sorted groups into bigger sorted groups by comparing top players from each.
5. Eventually, merge all groups into **one final sorted lineup** — strongest to weakest.

---

This reflects the essence of **Merge Sort** —  
break the problem down, solve each part, and **merge solutions** in a structured way.

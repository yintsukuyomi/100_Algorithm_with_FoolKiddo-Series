## ✅ What is Bubble Sort?

### Bubble Sort is a simple comparison-based sorting algorithm.

It works by repeatedly comparing adjacent elements and swapping them if they are in the wrong order. After each pass, the largest (or smallest) element "bubbles" up to its correct position.

---

### 📊 Time & Space Complexity

- **Worst Case:** O(n²)  
- **Best Case:** O(n) (if already sorted)  
- **Average Case:** O(n²)  
- **Space Complexity:** O(1) *(in-place sorting)*

---

## 🧠 Algorithm Steps:

1. Start from the **first element**.
2. Compare the current element with the **next element**.
3. If the current element is **greater than the next**, **swap** them.
4. Move to the **next pair of elements** and repeat the process.
5. After each pass, the **largest element** "bubbles up" to the end of the array.
6. Repeat the process for the remaining unsorted portion of the array.
7. Stop when no more swaps are needed (the array is fully sorted).

---

## 🫧 Real-Life Analogy: *"Kids Lining Up by Height"*

Imagine you have a group of kids standing in a **random order**, and your goal is to line them up from **shortest to tallest**.

---

### 🔁 How would you do it manually?

1. You look at the **first two kids** in line.
2. If the one on the **left is taller** than the one on the right, they **swap places**.
3. Move one step to the right and **repeat the comparison**.
4. By the end of the first pass, the **tallest kid "bubbles up" to the end**.
5. On the next pass, repeat the process, but **ignore the last (already sorted) kid**.
6. Keep going until **no more swaps are needed** — now the line is fully sorted.

---

This is the essence of **Bubble Sort** — simple, logical, and step-by-step.

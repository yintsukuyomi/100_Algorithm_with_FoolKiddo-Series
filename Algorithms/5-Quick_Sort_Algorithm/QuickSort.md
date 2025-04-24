## ✅ What is Quick Sort?

### Quick Sort is a highly efficient, comparison-based **divide and conquer** sorting algorithm.

It works by selecting a **pivot** element from the array and **partitioning** the other elements into two sub-arrays — one with elements **less than the pivot**, and one with elements **greater than the pivot**. These sub-arrays are then **recursively sorted**.

---

### 📊 Time & Space Complexity

- **Worst Case:** O(n²) *(when the pivot is always the smallest or largest element)*  
- **Best Case:** O(n log n) *(when the pivot splits the array evenly)*  
- **Average Case:** O(n log n)  
- **Space Complexity:** O(log n) *(in-place, recursive stack space)*

---

## 🧠 Algorithm Steps:

1. **Choose a pivot** element from the array.
2. **Partition** the array into two subarrays:
   - Elements **less than** the pivot.
   - Elements **greater than** the pivot.
3. Recursively apply **Quick Sort** to the subarrays.
4. Combine the sorted subarrays and the pivot to form the final sorted array.

---

## ⚔️ Real-Life Analogy: *"Organizing Books Around a Reference Book"*

Imagine you're organizing books in a library, and you pick **one book** as a reference point — say, by its title.

---

### 🔁 How would you do it manually?

1. Choose a book (pivot) and place it on the table.
2. Scan the other books:
   - Place books with **titles before** the pivot to the **left**.
   - Place books with **titles after** the pivot to the **right**.
3. Now, repeat the process for the **left and right groups** independently.
4. Once each group is sorted, your books will be in **alphabetical order** with the pivot in its **correct position**.

---

This is the essence of **Quick Sort** —  
**divide using a pivot**, sort each side, and let the recursion do the rest.

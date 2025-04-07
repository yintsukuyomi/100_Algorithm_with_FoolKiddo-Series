## ✅ What is Binary Search?

### Binary Search is a highly efficient comparison-based search algorithm.

It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the search continues on the left half, or if it's greater, it continues on the right half. This process repeats until the value is found or the interval is empty.

---

### 📊 Time & Space Complexity

- **Worst Case:** O(log n)  
- **Best Case:** O(1)  
- **Average Case:** O(log n)  
- **Space Complexity:** O(1) *(in-place search)*

---

## 🧠 Algorithm Steps:

1. Start with the **entire array**.
2. Find the **middle element** of the array.
3. If the target element is **equal** to the middle element, **return** the index.
4. If the target element is **less** than the middle element, repeat the search on the **left half**.
5. If the target element is **greater** than the middle element, repeat the search on the **right half**.
6. Repeat the process until the target is found or the interval is empty.

---

## ✅ Real-Life Analogy: *"Searching for a Book in a Library"*

Imagine you're in a library, and the books are sorted in **alphabetical order**.  
Your goal is to find a **specific book**.

---

### 🔁 How would you do it manually?

1. Start by looking at the **middle book** on the shelf.
2. If the book you're searching for is **alphabetically before** the middle book,  
   you know the book must be in the **left half** of the shelf.
3. If the book you're looking for is **alphabetically after** the middle book,  
   it must be in the **right half** of the shelf.
4. Keep **dividing the shelf into halves** and repeating the process,  
   always focusing on the **middle book** of the remaining section,  
   until you find the book or narrow down to one last option.
5. This method **reduces** the number of books you need to search through at each step,  
   making it **faster than searching book by book**.

---

You keep **dividing the search space in half** until you find the book —  
that's the essence of **Binary Search**.

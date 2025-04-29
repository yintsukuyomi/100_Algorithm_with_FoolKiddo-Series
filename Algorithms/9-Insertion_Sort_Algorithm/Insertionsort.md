## ✅ What is Insertion Sort?

### Insertion Sort is a simple comparison-based sorting algorithm that builds the final sorted array **one element at a time**.

It works similarly to the way we **sort playing cards** in our hands.

---

### 📊 Time & Space Complexity

- **Worst Case:** O(n²)  
- **Best Case:** O(n) *(when the array is already sorted)*  
- **Average Case:** O(n²)  
- **Space Complexity:** O(1) *(in-place sorting)*

---

## 🧠 Algorithm Steps:

1. Start with the **second element** (the first element is trivially sorted).
2. **Compare** it with the elements before it.
3. **Shift** larger elements **one position to the right**.
4. **Insert** the current element into its correct position.
5. Move to the **next element** and repeat until the entire array is sorted.

---

## ✅ Real-Life Analogy: *"Sorting Playing Cards in Your Hand"*

Imagine you're playing a card game, and you're **holding cards** in your hand.  
You want to arrange them **from smallest to largest**.

---

### 🔁 How would you do it manually?

1. You **pick up one card at a time** from the deck.
2. You **compare** it with the cards already in your hand (which are sorted).
3. **Shift** the cards that are larger to make space.
4. **Insert** the new card into the correct position.
5. Repeat the process until **all cards are sorted** in your hand.

---

This describes the essence of **Insertion Sort** —  
**gradually building a sorted list** by **inserting elements** into the correct place one by one.

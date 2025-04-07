# Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current index is the smallest

        # Find the actual smallest element in the rest of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap if a smaller element was found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Helper function to print the array
def print_array(arr):
    print(" ".join(map(str, arr)))

# Main method
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]

    print("Unsorted array:")
    print_array(data)

    selection_sort(data)  # Call Selection Sort

    print("Sorted array:")
    print_array(data)

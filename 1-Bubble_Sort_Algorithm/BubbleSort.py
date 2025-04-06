# Bubble Sort Code
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Outer loop for each pass
        swapped = False  # Flag to check if any swapping occurred in this pass

        # Inner loop for comparing adjacent elements
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                # Swap if the current element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set flag to true if swapping occurred

        # If no two elements were swapped in the inner loop, then break
        if not swapped:
            break  # Array is already sorted

# Helper method to print the array
def print_array(arr):
    for value in arr:
        print(value, end=" ")  # Print each element followed by a space
    print()  # Move to the next line after printing all elements

# Main method: Entry point of the program
if __name__ == "__main__":
    # Example usage
    data = [64, 34, 25, 12, 22, 11, 90]

    print("Unsorted array:")
    print_array(data)  # Print the unsorted array

    # Calling the bubble_sort function
    bubble_sort(data)

    print("Sorted array:")
    print_array(data)  # Print the sorted array

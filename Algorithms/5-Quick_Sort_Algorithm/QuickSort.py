# Quick Sort Algorithm
def quick_sort(arr):
    if len(arr) <= 1: # Base case: if the array is empty or has one element, it's already sorted
        return arr
    
    pivot = arr[len(arr) // 2] # Choose the pivot element (middle element in this case)
    left = [x for x in arr if x < pivot] # Elements less than the pivot
    middle = [x for x in arr if x == pivot] # Elements equal to the pivot
    right = [x for x in arr if x > pivot] # Elements greater than the pivot
    
    return quick_sort(left) + middle + quick_sort(right) # Recursively sort and combine

# Helper function to print the array
def print_array(arr):
    print(" ".join(map(str, arr))) # Print the array elements separated by spaces


# Main function to test the quick sort algorithm
if __name__ == "__main__":
    data = [38, 27, 43, 31, 9, 82, 10] # Example array to be sorted
    print("Unsorted array:")
    print_array(data) # Print the unsorted array

    sorted_arr = quick_sort(data) # Sort the array using quick sort
    print("Sorted array:")
    print_array(sorted_arr) # Print the sorted array
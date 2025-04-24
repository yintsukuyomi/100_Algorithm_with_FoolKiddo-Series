# Merge Sort Algorihm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr # Base case: if the array is empty or has one element, it's already sorted
    
    mid = len (arr) // 2 # Find the middle index of the array
    left_half = merge_sort(arr[:mid]) # Recursively sort the left half
    right_half = merge_sort(arr[mid:]) # Recursively sort the right half

    return merge(left_half, right_half) # Merge the sorted halves

# Merge two sorted arrays into a single sorted array
def merge(left, right):
    sorted_array = [] # Initialize an empty array to hold the merged result
    i = j = 0 # Initialize pointers for both arrays

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add any remaining elements 
    sorted_array.extend(left[i:]) # Add remaining elements from the left array
    sorted_array.extend(right[j:]) # Add remaining elements from the right array

    return sorted_array # Return the merged sorted array

# Helper function to print the array
def print_array(arr):
    print(" ".join(map(str, arr))) # Print the array elements separated by spaces

# Main function to test the merge sort algorithm	
if __name__ == "__main__":
    arr = [38, 27, 43, 31, 9, 82, 10] # Example array to be sorted
    print("Unsorted array:")
    print_array(arr) # Print the unsorted array

    sorted_arr = merge_sort(arr) # Sort the array using merge sort
    print("Sorted array:")
    print_array(sorted_arr) # Print the sorted array

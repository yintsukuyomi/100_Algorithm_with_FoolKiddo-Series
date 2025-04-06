# Binary Search Code

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 # Index in the middle

        # If the element we are looking for is equal to the middle element
        if arr[mid] == target:
            return mid # We found it!!!

        # If the element we are looking for is smaller than the middle element, examine the right half
        elif arr[mid] > target:
            high = mid - 1 #We go down to the right half

        # If the element we are looking for is greater than the middle element, examine the left half

        else:
            low = mid + 1 # We go down to the left half

    return -1 #If the element not found, return -1

    #Helper method to print the results
def print_result(index):
    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found in the array")
    
#Main method: Entry point of the program
if __name__ == "__main__":
    data = [11, 12, 22, 25, 34, 64, 90]  # An sorted array for binary search

    target = 22  # Element we looking for
    print("Array:")
    print(data)

    # Call Binary Search
    result = binary_search(data, target)

    # Print result
    print_result(result)

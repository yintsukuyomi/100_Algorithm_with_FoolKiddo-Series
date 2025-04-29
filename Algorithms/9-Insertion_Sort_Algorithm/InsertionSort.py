def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\n---\nStarting i={i}, key={key}")

        while j >= 0 and arr[j] > key:
            print(f"  Comparing arr[{j}]={arr[j]} > key={key}: moving arr[{j}] to arr[{j+1}]")
            arr[j + 1] = arr[j]
            j -= 1
            print(f"  New j={j}")

        arr[j + 1] = key
        print(f"Inserted key={key} at position {j+1}")
        print(f"Array now: {arr}")

if __name__ == "__main__":
    data = [9, 5, 2, 4, 3]
    print("Unsorted Array:")
    print(data)

    insertion_sort(data)

    print("Sorted Array:")
    print(data)

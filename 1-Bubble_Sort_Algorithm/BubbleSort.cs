using System;

class BubbleSortExample
{
    // Bubble Sort Code
    public static void BubbleSort(int[] arr)
    {
        int n = arr.Length;
        for (int i = 0; i < n - 1; i++) // Outer loop for each pass
        {
            bool swapped = false; // Flag to check if any swapping occurred in this pass

            // Inner loop for comparing adjacent elements
            for (int j = 0; j < n - i - 1; j++)
            {
                if (arr[j] > arr[j + 1]) // Compare adjacent elements
                {
                    // Swap if the current element is greater than the next element
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true; // Set flag to true if swapping occurred
                }
            }

            // If no two elements were swapped in the inner loop, then break
            if (!swapped)
            {
                break; // Array is already sorted
            }
        }
    }

    // Helper method to print the array
    public static void PrintArray(int[] arr)
    {
        foreach (int value in arr)
        {
            Console.Write(value + " "); // Print each element followed by a space
        }
        Console.WriteLine(); // Move to the next line after printing all elements
    }

    // Main method: Entry point of the program
    static void Main()
    {
        // Example usage
        int[] data = { 64, 34, 25, 12, 22, 11, 90 };

        Console.WriteLine("Unsorted array:");
        PrintArray(data); // Print the unsorted array

        // Calling the BubbleSort function
        BubbleSort(data);

        Console.WriteLine("Sorted array:");
        PrintArray(data); // Print the sorted array
    }
}
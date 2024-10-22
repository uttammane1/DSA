def merge_sort_desc(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the array into two halves
        right_half = arr[mid:]

        # Recursive calls to sort both halves
        merge_sort_desc(left_half)
        merge_sort_desc(right_half)

        # Merge the sorted halves in descending order
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:  # Reverse comparison
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Input reading
n = int(input())  # Number of elements
arr = list(map(int, input().split()))  # Reading the list of n integers

# Sorting the array using Merge Sort in descending order
merge_sort_desc(arr)

# Output the sorted array in descending order
print(" ".join(map(str, arr)))

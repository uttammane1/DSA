def quick_sort(arr, low, high):
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the correct place
        pi = partition(arr, low, high)

        # Separately sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # pivot element
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:  # Elements smaller than pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Input reading
n = int(input())  # Number of elements
arr = list(map(int, input().split()))  # Reading the list of n integers

# Sorting the array using Quick Sort
quick_sort(arr, 0, n - 1)

# Output the sorted array in ascending order
print(" ".join(map(str, arr)))

def selectionSort(N, arr):
    for i in range(N):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = selectionSort(N, arr)
print(*sorted_arr)
def bubbleSort(N, arr):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = bubbleSort(N, arr)
print(*sorted_arr)

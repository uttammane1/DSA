def moduloSort(N, k, arr):
    sorted_arr = sorted(arr, key=lambda x: (x % k, arr.index(x)))
    return sorted_arr

N, k = map(int, input().split())
arr = list(map(int, input().split()))
sorted_arr = moduloSort(N, k, arr)
print(*sorted_arr)
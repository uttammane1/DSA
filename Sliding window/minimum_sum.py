def min_sum_k_consecutive(n, k, arr):
    current_sum = sum(arr[:k])
    min_sum = current_sum
    
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        min_sum = min(min_sum, current_sum)
    
    return min_sum

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_sum_k_consecutive(n, k, arr))

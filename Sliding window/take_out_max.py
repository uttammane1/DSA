def max_sum_subarray(n, k, arr):
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    for i in range(k, n):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(max_sum_subarray(n, k, arr))
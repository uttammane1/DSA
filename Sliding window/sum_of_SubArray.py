def has_subarray_with_sum_k(n, k, arr):
    current_sum = 0
    sum_set = set()
    
    for num in arr:
        current_sum += num
        
        if current_sum == k or (current_sum - k) in sum_set:
            return "Yes"
        
        sum_set.add(current_sum)
    
    return "No"

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(has_subarray_with_sum_k(n, k, arr))

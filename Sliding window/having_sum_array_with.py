def count_subarrays_with_sum_less_than_m(n, m, arr):
    start = 0
    current_sum = 0
    count = 0
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum >= m and start <= end:
            current_sum -= arr[start]
            start += 1
        
        count += end - start + 1
    
    return count

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_subarrays_with_sum_less_than_m(n, m, arr))

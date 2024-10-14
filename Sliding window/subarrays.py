def count_even_subarrays(n, arr):
    even_count = 0
    odd_count = 0
    prefix_sum = 0
    total_even_subarrays = 0
    
    for num in arr:
        prefix_sum += num
        
        if prefix_sum % 2 == 0:
            total_even_subarrays += 1 + even_count
            even_count += 1
        else:
            total_even_subarrays += odd_count
            odd_count += 1
            
    return total_even_subarrays

n = int(input())
arr = list(map(int, input().split()))
print(count_even_subarrays(n, arr))

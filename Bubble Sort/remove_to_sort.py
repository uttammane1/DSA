def removeToSort(arr):
    result = []
    last = float('-inf')
    
    for num in arr:
        if num >= last:  # Allow non-strictly increasing order (>= instead of >)
            result.append(num)
            last = num
            
    return result

n = int(input())  # Input the length of the array
arr = list(map(int, input().split()))  # Input the array elements
sorted_arr = removeToSort(arr)
print(*sorted_arr)
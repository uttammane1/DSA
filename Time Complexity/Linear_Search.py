def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

arr = [3, 5, 2, 9, 6]
target = 9
print(linear_search(arr, target))  

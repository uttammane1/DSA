def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

arr = [3, 5, 2, 9, 6]
print(find_max(arr))  
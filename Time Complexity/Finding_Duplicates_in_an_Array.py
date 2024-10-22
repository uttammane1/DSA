def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

arr = [1, 2, 3, 4, 5, 6, 3]
print(has_duplicates(arr))  
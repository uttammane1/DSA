def search_range(nums, target):
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return bound

    first = find_bound(True)
    last = find_bound(False)

    return [first, last]

nums = [5, 7, 7, 8, 8, 10]
target = 8
result = search_range(nums, target)
print(result)  

def find_subsets(nums):
    result = []
    subset = []

    def backtrack(index):
        if index == len(nums):
            result.append(subset[:])
            return
        subset.append(nums[index])
        backtrack(index + 1)
        subset.pop()
        backtrack(index + 1)

    backtrack(0)
    return result

nums = [1, 2, 3]
print("Subsets:", find_subsets(nums))

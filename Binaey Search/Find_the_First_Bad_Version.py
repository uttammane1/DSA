def first_bad_version(n, isBadVersion):
    left, right = 1, n

    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

def isBadVersion(version):
    return version >= 4

n = 5
result = first_bad_version(n, isBadVersion)
print(result)  
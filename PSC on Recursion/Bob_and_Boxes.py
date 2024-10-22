def count_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_ways(n - 1) + count_ways(n - 3) + count_ways(n - 5)

n = int(input())  # Read the number of boxes
print(count_ways(n))  # Output the result

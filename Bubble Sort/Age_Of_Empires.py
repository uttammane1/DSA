def maxAssociationSpeed(workers):
    workers.sort()
    result = 0
    for i in range(0, len(workers), 2):
        result += workers[i]
    return result

# Input reading
n = int(input())  # Number of associations
workers = list(map(int, input().split()))  # Speeds of the 2N workers

# Calculate and print the result
print(maxAssociationSpeed(workers))

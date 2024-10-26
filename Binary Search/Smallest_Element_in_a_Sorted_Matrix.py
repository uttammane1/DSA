import heapq

def kth_smallest(matrix, k):
    n = len(matrix)
    min_heap = []

    # Add the first element of each row to the min-heap
    for i in range(min(k, n)):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))

    # Extract-min k-1 times
    for _ in range(k - 1):
        val, row, col = heapq.heappop(min_heap)
        if col + 1 < n:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

    return heapq.heappop(min_heap)[0]

matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
result = kth_smallest(matrix, k)
print(result)  

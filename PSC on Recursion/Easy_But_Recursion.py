def array_sum(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n-1] + array_sum(arr, n-1)

t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Number of integers in this test case
    arr = list(map(int, input().split()))  # Array of integers
    print(array_sum(arr, n))

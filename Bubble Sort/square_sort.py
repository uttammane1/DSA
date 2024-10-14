def squareSort(arr):
    sorted_arr = sorted(arr, key=lambda x: x * x)
    return sorted_arr

T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Size of the array
    arr = list(map(int, input().split()))  # Array elements
    sorted_arr = squareSort(arr)
    print(*sorted_arr)

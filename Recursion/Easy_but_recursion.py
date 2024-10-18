def recursive_sum(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n - 1] + recursive_sum(arr, n - 1)

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        print(recursive_sum(arr, n))

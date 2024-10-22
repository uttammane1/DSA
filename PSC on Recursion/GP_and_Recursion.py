def geometric_sum(n, r):
    if n == 0:
        return 1
    else:
        return (1 / (r ** n)) + geometric_sum(n - 1, r)

n, r = map(int, input().split())
result = geometric_sum(n, r)
print(f"{result:.4f}")
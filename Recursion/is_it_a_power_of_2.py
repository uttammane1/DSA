def is_power_of_two(n):
    return (n > 0) and (n & (n - 1)) == 0

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        if is_power_of_two(n):
            print("YES")
        else:
            print("NO")

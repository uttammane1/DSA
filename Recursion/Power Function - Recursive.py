def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half_power = power(a, b // 2)
        return half_power * half_power
    else:
        return a * power(a, b - 1)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(power(a, b))

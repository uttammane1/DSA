def can_make_money(n):
    while n > 1:
        if n % 10 == 0:
            n //= 10
        elif n % 20 == 0:
            n //= 20
        else:
            return "No"
    return "Yes" if n == 1 else "No"

# Reading number of test cases
t = int(input())
for _ in range(t):
    n = int(input())
    print(can_make_money(n))

# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
def super_digit(n):
    if len(n) == 1:
        return int(n)
    else:
        digit_sum = sum(int(digit) for digit in n)
        return super_digit(str(digit_sum))

# Input handling
t = int(input())  # Number of test cases
for _ in range(t):
    n = input().strip()  # Read the number N as a string
    print(super_digit(n))

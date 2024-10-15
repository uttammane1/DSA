def check_palindrome(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    if s == reversed_str:
        print("YES")
    else:
        print("NO")

# Input
s = input().strip()
check_palindrome(s)

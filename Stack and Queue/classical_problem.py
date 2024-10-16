def is_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return "not balanced"
    
    return "balanced" if not stack else "not balanced"

t = int(input())
for _ in range(t):
    s = input().strip()
    print(is_balanced(s))

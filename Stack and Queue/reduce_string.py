def reduce_string(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove matching adjacent characters
        else:
            stack.append(char)
    
    result = ''.join(stack)
    if result:
        print(result)
    else:
        print("Empty String")

# Input
s = input().strip()
reduce_string(s)

def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

def runProgram(input):
    lines = input.split("\n")
    T = int(lines[0])
    result = []
    index = 1
    
    for _ in range(T):
        n = int(lines[index])  # Read length of string (not used)
        s = lines[index + 1]   # Read the string
        result.append(remove_adjacent_duplicates(s))
        index += 2
    
    for res in result:
        print(res)

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read()
    runProgram(input_data)

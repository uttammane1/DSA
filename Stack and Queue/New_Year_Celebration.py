from collections import deque

def runProgram(input):
    lines = input.split("\n")
    Q = int(lines[0])
    
    queue = deque()
    stack = []

    output = []

    for i in range(1, Q + 1):
        query = lines[i].split()

        if query[0] == '1':
            queue.append(int(query[1]))
        elif query[0] == '2':
            stack.append(int(query[1]))
        elif query[0] == '3':
            if queue:
                output.append(queue[0])
            else:
                output.append(-1)
        elif query[0] == '4':
            if stack:
                output.append(stack[-1])
            else:
                output.append(-1)
        elif query[0] == '5':
            if queue:
                person = queue.popleft()
                stack.append(person)
            else:
                output.append(-1)

    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read()
    runProgram(input_data)

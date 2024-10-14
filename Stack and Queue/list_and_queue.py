def runProgram(input):
    lines = input.split("\n")
    t = int(lines[0])
    queue = []

    for i in range(1, t + 1):
        command = lines[i].split()
        
        if command[0] == 'E':
            queue.append(int(command[1]))
        elif command[0] == 'D':
            if queue:
                print(queue.pop(0))
            else:
                print("Empty")

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read()
    runProgram(input_data)

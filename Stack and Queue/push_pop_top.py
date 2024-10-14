def run_program(input):
    # Split the input into lines
    lines = input.strip().split("\n")
    n = int(lines[0])  # The number of operations
    stack = []  # Initialize an empty stack

    # Loop through each operation
    for i in range(1, n + 1):
        query = lines[i].split(" ")

        if query[0] == '1':
            # Push operation: Add to the stack
            stack.append(int(query[1]))
        elif query[0] == '2':
            # Pop operation: Remove from the top if stack is not empty
            if stack:
                stack.pop()
        elif query[0] == '3':
            # Print the top element or "Empty!" if stack is empty
            if stack:
                print(stack[-1])
            else:
                print("Empty!")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_program("6\n1 15\n1 20\n2\n3\n2\n3")
    else:
        input_data = []
        try:
            while True:
                line = input()
                input_data.append(line)
        except EOFError:
            # Join all input lines and run the program
            run_program("\n".join(input_data))

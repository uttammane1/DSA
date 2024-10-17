def waiting_line(operations):
    queue = []
    results = []

    for operation in operations:
        if operation[0] == 'E':
            x = operation[1]
            queue.append(x)
            results.append(len(queue))
        elif operation[0] == 'D':
            if queue:
                removed_element = queue.pop(0)
                results.append(f"{removed_element} {len(queue)}")
            else:
                results.append("-1 0")

    print('\n'.join(map(str, results)))

def run_program(input):
    lines = input.strip().split('\n')
    N = int(lines[0].strip())
    operations = [line.strip().split() if line[0] == 'E' else [line.strip()] for line in lines[1:N + 1]]
    waiting_line(operations)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    run_program(input())

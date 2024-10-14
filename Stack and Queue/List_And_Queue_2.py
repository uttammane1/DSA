import queue

def runProgram(input):
    lines = input.split("\n")
    t = int(lines[0])
    
    q1 = queue.Queue()
    q2 = queue.Queue()
    
    output = []

    for i in range(1, t + 1):
        command = lines[i].split()

        if command[0] == 'Push':
            q1.put(int(command[1]))
        elif command[0] == 'Pop':
            if q1.empty():
                output.append('Empty')
            else:
                # Transfer all elements except the last to the second queue
                while q1.qsize() > 1:
                    q2.put(q1.get())
                # Get the last element
                last_element = q1.get()
                output.append(last_element)
                # Swap the queues
                q1, q2 = q2, q1

    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read()
    runProgram(input_data)

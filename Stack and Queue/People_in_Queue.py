def people_in_queue(K, queries):
    queue = []
    results = []

    for query in queries:
        if query[0] == 1:
            identity = query[1]
            if len(queue) < K:
                queue.append(identity)
                results.append(identity)
            else:
                results.append(-1)
        elif query[0] == 2:
            if queue:
                results.append(queue.pop(0))
            else:
                results.append(-1)

    print('\n'.join(map(str, results)))

def run_program(input):
    lines = input.strip().split('\n')
    K, Q = map(int, lines[0].strip().split())
    queries = [list(map(int, lines[i].strip().split())) for i in range(1, Q + 1)]
    people_in_queue(K, queries)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    run_program(input())

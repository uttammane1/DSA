def valid_stack_sequence(test_cases):
    results = []
    for case in test_cases:
        n, pushed, popped = case
        stack = []
        j = 0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        results.append("YES" if j == n else "NO")
    return '\n'.join(results)

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    test_cases.append((n, pushed, popped))

print(valid_stack_sequence(test_cases))

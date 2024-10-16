def next_smaller_of_next_greater(test_cases):
    results = []
    for case in test_cases:
        N, arr = case
        next_greater = [-1] * N
        stack = []

        for i in range(N):
            while stack and arr[stack[-1]] < arr[i]:
                next_greater[stack.pop()] = i
            stack.append(i)

        next_smaller_of_next_greater = [-1] * N
        stack = []

        for i in range(N):
            if next_greater[i] != -1:
                next_greater_index = next_greater[i]
                while stack and arr[stack[-1]] >= arr[next_greater_index]:
                    stack.pop()
                next_smaller_of_next_greater[i] = arr[stack[-1]] if stack else -1
            stack.append(i)

        results.append(' '.join(map(str, next_smaller_of_next_greater)))

    return '\n'.join(results)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((N, arr))

print(next_smaller_of_next_greater(test_cases))

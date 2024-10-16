def stock_span(prices, N):
    stack = []
    spans = [0] * N
    
    for i in range(N):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    
    return spans

# Input
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    result = stock_span(prices, N)
    print(' '.join(map(str, result)))

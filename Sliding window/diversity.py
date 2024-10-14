def max_families_within_diversity(n, k, incomes):
    incomes.sort()
    left = 0
    max_families = 0
    
    for right in range(n):
        while incomes[right] - incomes[left] > k:
            left += 1
        max_families = max(max_families, right - left + 1)
    
    return max_families

t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    incomes = list(map(int, input().split()))
    results.append(max_families_within_diversity(n, k, incomes))

for result in results:
    print(result)

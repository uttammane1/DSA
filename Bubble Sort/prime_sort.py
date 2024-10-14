def sieve_distinct_prime_factors(limit):
    prime_factors_count = [0] * (limit + 1)
    
    for i in range(2, limit + 1):
        if prime_factors_count[i] == 0:  # i is a prime number
            for multiple in range(i, limit + 1, i):
                prime_factors_count[multiple] += 1
    
    return prime_factors_count

def prime_sort(arr):
    limit = max(arr)
    prime_factors_count = sieve_distinct_prime_factors(limit)
    
    sorted_arr = sorted(arr, key=lambda x: (prime_factors_count[x], x))
    
    return sorted_arr

# Input reading
n = int(input())  # Size of the array
arr = list(map(int, input().split()))  # Elements in the array

# Get the sorted array based on distinct prime factors
sorted_array = prime_sort(arr)

# Print the output
print(" ".join(map(str, sorted_array)))

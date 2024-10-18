# Function to calculate factorial using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Main code to take input and print the output
if __name__ == "__main__":
    N = int(input().strip())
    
    print(factorial(N))

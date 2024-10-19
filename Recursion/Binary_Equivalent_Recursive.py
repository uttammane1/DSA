# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
def to_binary(n):
    if n == 0:
        return ''
    else:
        return to_binary(n // 2) + str(n % 2)

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        binary_representation = to_binary(n)
        # If n is 0, explicitly return "0" since the recursive function returns an empty string for n=0
        print(binary_representation if binary_representation else "0")

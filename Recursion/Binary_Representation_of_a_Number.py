def binary_representation(n):
    return bin(n)[2:]

if __name__ == "__main__":
    N = int(input().strip())
    print(binary_representation(N))

def longestSubstring(s, k):
    if len(s) == 0:
        return 0
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in char_count:
        if char_count[char] < k:
            return max(longestSubstring(substring, k) for substring in s.split(char))
    
    return len(s)

n = int(input())
s = input().strip()
k = int(input())
print(longestSubstring(s, k))

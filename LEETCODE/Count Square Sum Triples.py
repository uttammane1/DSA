class Solution(object):
    def countTriples(self, n):
        count = 0
        squares = set(i * i for i in range(1, n + 1))

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a*a + b*b in squares:
                    count += 1

        return count

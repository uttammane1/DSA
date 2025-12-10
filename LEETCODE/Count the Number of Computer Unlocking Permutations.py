class Solution(object):
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity) + 1

        # dp[i][j] = number of ways using i numbers
        # with the j-th smallest number at the end
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[1][0] = 1

        for i in range(2, n + 1):
            prefix = [0] * (i)
            prefix[0] = dp[i - 1][0]

            for j in range(1, i - 1):
                prefix[j] = (prefix[j - 1] + dp[i - 1][j]) % MOD

            if complexity[i - 2] == 1:  # increasing
                for j in range(i):
                    if j > 0:
                        dp[i][j] = prefix[j - 1]
            else:  # decreasing
                for j in range(i):
                    dp[i][j] = (prefix[i - 2] - (prefix[j - 1] if j > 0 else 0)) % MOD

        return sum(dp[n][:n]) % MOD

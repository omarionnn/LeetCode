class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}


        def helper(i):
            if i <= 1:
                return 1

            if i in cache:
                return cache[i]

            cache[i] = helper(i - 1) + helper(i - 2)
            return cache[i]

        return helper(n)

        

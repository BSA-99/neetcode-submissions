class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}

        def dp(n):
            
            if n<=2:
                return n
            
            if n in memory:
                return memory[n]
            
            memory[n] = dp(n-1) + dp(n-2)

            return memory[n]
        return dp(n)
        
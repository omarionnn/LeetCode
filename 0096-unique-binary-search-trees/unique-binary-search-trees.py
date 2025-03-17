class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize a DP array where dp[i] represents the number of 
        # unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases:
        # - There is exactly 1 way to construct a BST with 0 nodes (empty tree)
        # - There is exactly 1 way to construct a BST with 1 node
        dp[0] = 1
        dp[1] = 1
        
        # Fill the DP array by calculating the number of unique BSTs for each size from 2 to n
        for i in range(2, n + 1):
            # For each value j that could be the root (1 to i)
            for j in range(1, i + 1):
                # The left subtree will have j-1 nodes (values from 1 to j-1)
                # The right subtree will have i-j nodes (values from j+1 to i)
                # The total number of unique BSTs with root j is the product of these two numbers
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]
            
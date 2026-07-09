class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        dp=[[None for _ in range(n)] for _ in range(n)]
        def solve(i,j):
            if j<0 or j>=n:
                return float('inf')
            if i==n-1:
                return matrix[i][j]
            if dp[i][j]!=None:
                return dp[i][j]
            l=solve(i+1,j-1)
            s=solve(i+1,j)
            r=solve(i+1,j+1)

            dp[i][j]=min(l,s,r)+matrix[i][j]
            return dp[i][j]
        res=float('inf')
        for i in range(n):
            res=min(res,solve(0,i))
        return res
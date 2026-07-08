class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # def solve(i,j):
        #     if i==0 and j==0:
        #         return grid[i][j]
        #     if i<0 or j<0:
        #         return float('inf')

        #     if dp[i][j]!=0:
        #         return dp[i][j]


        #     left=grid[i][j]+solve(i,j-1)
        #     up=grid[i][j]+solve(i-1,j)
        #     dp[i][j]=min(left,up)
        #     return dp[i][j]
        
        # return solve(len(grid)-1,len(grid[0])-1)


        # ------------2-----------------------
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    up=float('inf')
                    left=float('inf')
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    dp[i][j]=min(up,left)+grid[i][j]

        return dp[len(grid)-1][len(grid[0])-1]

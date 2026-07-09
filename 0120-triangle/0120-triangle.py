class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp=[[None for _ in range(len(triangle))] for _ in range(len(triangle))]
        def solve(i,j):
            if i==len(triangle)-1:
                return triangle[i][j]
            if dp[i][j]!=None:
                return dp[i][j]

            left=solve(i+1,j)
            right=solve(i+1,j+1)
            dp[i][j]=min(left,right)+triangle[i][j]
            return dp[i][j]
        return solve(0,0)

        # -----------2-------------------


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp=[[0 for _ in range(len(nums))] for _ in range(len(nums))]
        # def solve(idx,jumps):
        #     if idx>=len(nums)-1:
        #         return jumps
        #     if dp[idx][jumps]:
        #         return dp[idx][jumps]
        #     minjumps=float('inf')
        #     for i in range(1,nums[idx]+1):
        #         minjumps=min(solve(i+idx,jumps+1),minjumps)
        #     dp[idx][jumps]=minjumps
        #     return minjumps
        
        # return solve(0,0)


        # --------------2------------------
        l=0
        r=0
        jumps=0
        while r<len(nums)-1:
            far=0
            for i in range(l,r+1):
                far=max(i+nums[i],far)
            l=r+1
            r=far
            jumps+=1

        return jumps
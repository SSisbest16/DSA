class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m= -inf

        c=0

        for i in nums:
            c=max(i,c+i)
            m=max(m,c)
        return m    
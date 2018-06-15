class Solution(object):
    def maxSubArray(self, nums):
        sum_cont = 0
        if not nums:
            return sum_cont
        sum_cont = nums[0]
        max_cont = nums[0]
        for idx,i in enumerate(nums[1:]):
            sum_cont = max(sum_cont+i,i)
            if sum_cont > max_cont:
                max_cont = sum_cont
        return max_cont 
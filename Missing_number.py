class Solution(object):
    def missingNumber(self, nums):
        if not nums:
            return 0
        n = len(nums)
        sum_n = n*(n+1)/2
        return sum_n-sum(nums)
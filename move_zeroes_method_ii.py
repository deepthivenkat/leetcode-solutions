class Solution(object):
    def moveZeroes(self, nums):
        start = 0
        for idx,vals in enumerate(nums):
            if vals!=0:
                nums[idx], nums[start] = nums[start], nums[idx]
                start += 1
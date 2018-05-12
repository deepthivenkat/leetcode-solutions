class Solution(object):
    def moveZeroes(self, nums):
        non_zero_idx = [idx for idx,x in enumerate(nums) if x!=0 ]
        non_zero_len = len(non_zero_idx)
        start = 0
        for idx,vals in enumerate(nums):
            if start < non_zero_len:
                nums[idx] = nums[non_zero_idx[start]]
                start += 1
            else:
                nums[idx] = 0
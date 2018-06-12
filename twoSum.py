class Solution(object):
    def twoSum(self, nums, target):
        dict_nums = {}
        for idx,i in enumerate(nums):
            if target-i in dict_nums:
                return idx,dict_nums[target-i]
            else:
                dict_nums[i] = idx
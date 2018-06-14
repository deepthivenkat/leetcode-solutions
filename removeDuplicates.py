class Solution(object):
    def removeDuplicates(self, nums):
        len_nums = len(nums)
        if not nums:
            return 0
        start = 0
        i = 0
        while i < len_nums:
            if nums[start]==nums[i]:
                i+=1
            else:
                if start<len_nums-2:
                    nums[start+1]= nums[i]
                start +=1
                i+=1
        return start+1
        
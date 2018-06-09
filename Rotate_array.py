class Solution(object):
    def rotate(self, nums, k):
        len_nums = len(nums)
        if k ==0:
            return
        k = k%len_nums
        nums[:] = list(reversed(nums[:len_nums-k]))+list(reversed(nums[len_nums-k:]))
        nums[:] = reversed(nums)
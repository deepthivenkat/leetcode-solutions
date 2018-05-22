import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums:
            return None
        for idx,x in enumerate(nums):
            nums[idx] = -1*x
        heapq.heapify(nums)
        while k:
            c = heapq.heappop(nums)
            k-=1
        return -1*c
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums,len_nums = sorted(nums),len(nums)
        ans = sum(nums[:3])
        for i in xrange(0,len_nums):
            l,r = i+1, len_nums-1
            while l<r:
                three_sum = nums[i]+nums[l]+nums[r]
                if abs( three_sum-target)<abs(ans-target):
                    ans = three_sum
                if three_sum<target:
                    l+=1
                elif three_sum>target:
                    r-=1
                else:
                    return ans
        return ans
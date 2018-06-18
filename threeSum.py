class Solution(object):
    def threeSum(self, nums):
        nums,len_nums,res = sorted(nums),len(nums),[]
        for i in xrange(0,len_nums-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l,r = i+1, len_nums-1
            while l<r:
                three_sum = nums[i]+nums[l]+nums[r]
                if three_sum<0:
                    l+=1
                elif three_sum>0:
                    r-=1
                else:
                    res.append(sorted([nums[i],nums[r],nums[l]]))
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                    
        return res
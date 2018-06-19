class Solution(object):
    def maxArea(self, height):
        max_area,l,r = -1*float("inf"),0,len(height)-1
        while l<=r:
            max_area = max(max_area, min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
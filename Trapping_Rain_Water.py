class Solution(object):
    def trap(self, height):
        l,r,water,l_max,r_max = 0, len(height)-1,0,0,0
        while l<r:
            if height[l]> height[r]:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    water += r_max - height[r]
                r-=1
            else:
                if height[l]>l_max:
                    l_max = height[l]
                else:
                    water += l_max - height[l]
                l+=1
        return water
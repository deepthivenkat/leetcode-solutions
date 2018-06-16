import math
class Solution(object):
    def mySqrt(self, x):
        if x ==0 or x==1:
            return x
        l,r = 0,x
        while l<=r:
            mid = l + (r-l)//2
            sqrt = x/mid
            if sqrt < mid:
                r = mid-1
            elif sqrt > mid:
                l = mid+1
            else:
                return mid
        return r
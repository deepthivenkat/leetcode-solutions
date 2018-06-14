import math
class Solution(object):
    def mySqrt(self, x):
        r = x
        while r*r>x:
            r = (r+x//r)//2
        return int(r)
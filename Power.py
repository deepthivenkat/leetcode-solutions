class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return float(1)
        if x==0 or x==1:
            return x
        i,ret = 1,float(x)
        power = n if n>0 else -1*n
        while i < power:
            ret *= ret
            i = i*2
        for j in xrange(i-power):
            ret = ret/x
        return ret if n>0 else float(1)/ret
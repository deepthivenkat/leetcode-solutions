class Solution(object):
    def reverse(self, x):
        t_31 = pow(2,31)
        neg = 1
        if x <0:
            x = x*-1
            neg = -1
        rev = neg*int(''.join(reversed(str(x)))) 
        if rev>= -1*t_31 and rev <= t_31-1:
            return rev
        else:
            return 0
class Solution(object):
    def trailingZeroes(self, n):
        trail = 0
        while n > 1:
            by_5=n//5
            trail+=by_5
            n = by_5
        return trail
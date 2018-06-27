class Solution(object):
    def numJewelsInStones(self, J, S):
        if J and S:
            num = 0
            J = set(J)
            for stone in S:
                if stone in J:
                    num+=1
            return num
        else:
            return 0
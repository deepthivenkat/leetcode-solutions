from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        
        times1,times2 = defaultdict(list),defaultdict(list)
        for idx,charac in enumerate(s):
            times1[charac].append(idx)
        for idx,charac in enumerate(t):
            times2[charac].append(idx)
        for idx,charac in enumerate(t):
            char_s = s[idx]
            idx_s = times1[char_s]
            idx_t = times2[charac]
            if idx_s!=idx_t:
                return False
        return True
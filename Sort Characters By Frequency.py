from collections import Counter
class Solution:
    def frequencySort(self, s):
        c = Counter(s)
        new_str = ""
        while c:
            new_str += c.most_common(1)[0][0]*c.most_common(1)[0][1]
            del c[c.most_common(1)[0][0]]
        return new_str
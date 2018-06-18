from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        counter = Counter(words)
        res = sorted(counter, key=lambda x: (-counter[x],x))
        return res[:k]
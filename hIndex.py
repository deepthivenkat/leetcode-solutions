class Solution(object):
    def hIndex(self, citations):
        sorted_citations = sorted(citations,reverse=True)
        n = len(citations)
        h_idx = 0
        print sorted_citations
        for idx,i in enumerate(sorted_citations):
            if idx< i:
                h_idx = idx+1
        return h_idx
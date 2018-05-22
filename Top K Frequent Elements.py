from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        if not nums:
            return None
        len_nums = len(nums)
        if len_nums == k:
            return list(set(nums))
        freq_dict = defaultdict(list)
        count_dict = defaultdict(int)
        for x in nums:
            count_dict[x]+=1
        for key, v in count_dict.iteritems():
            freq_dict[v].append(key)
        count_k,result = 0,[]
        for i in range(len_nums,-1,-1):
            if freq_dict.get(i,None):
                val = freq_dict.get(i)
                while val:
                    result.append(val.pop())
                    count_k +=1
                if count_k >=k:
                    break
        result = result[:k]
        return result
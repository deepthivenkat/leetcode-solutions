class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i,m,len_s,ans=0,0,len(s),0
        idx_dict = {}
        for idx, i in enumerate(s):
            m = max(idx_dict.get(s[idx],0),m)
            idx_dict[i]=idx+1
            ans = max(ans,idx-m+1)
        return ans
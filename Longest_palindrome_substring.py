class Solution(object):
    def expandAroundCenter(self,s,i,j):
        len_s = len(s)
        if i>=0 and j<len_s and s[i]!=s[j]:
            return 0
        while i>=0 and j<len_s and s[i]==s[j]:
            i-=1
            j+=1
        return j-i-1
            
    def longestPalindrome(self, s):
        start,end = 0,0
        length = 0 if not s else 1
        for idx,i in enumerate(s):
            len_even = self.expandAroundCenter(s,idx,idx)
            len_odd = self.expandAroundCenter(s,idx,idx+1)
            length = max(len_even,len_odd)
            if length > end-start:
                start,end = idx-(length-1)/2, idx+length/2
        return s[start:end+1]
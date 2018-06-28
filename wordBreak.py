class Solution(object):
    def wordBreak(self, s, wordDict):
        len_s = len(s)
        arr = [False for i in range(len_s+1)]
        arr[0]=True
        i=0
        while i<=len_s:
            j=0
            while j<i:
                if arr[j] and s[j:i] in wordDict:
                    arr[i] = True
                j+=1
            i+=1 
        print arr
        return arr[-1]
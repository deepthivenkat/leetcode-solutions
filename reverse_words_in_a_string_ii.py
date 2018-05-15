class Solution(object):
    def reverseWords(self, str):
        len_s = len(str)
        for i in range(len_s//2):
            j = len_s-i-1
            str[i],str[j]=str[j],str[i]
        left = 0
        for idx, i in enumerate(str):
            if i==" ":
                str[left:idx]=reversed(str[left:idx])
                left = idx+1
        str[left:]= reversed(str[left:])
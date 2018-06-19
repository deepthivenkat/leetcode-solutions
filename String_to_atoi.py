class Solution(object):
    def myAtoi(self, str):
        str = list(str.strip())
        if not str:
            return 0
        idx,number = 0,0
        sign = -1 if str[idx]=="-" else 1
        if not str[idx].isdigit() and str[idx] not in ["+","-"]:
            return 0  
        idx= idx if str[idx].isdigit() and sign else idx+1
        print idx
        while idx<len(str) and str[idx].isdigit():
            number = number*10+ ord(str[idx])-ord("0")
            idx+=1
        return max(min(2**31-1,sign*number),-2**31)
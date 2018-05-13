class Solution(object):
    def isValid(self, s):
        len_s = len(s)
        if len_s%2!=0:
            return False 
        bracket_value = {"(":1, ")":-1, "{":2, "}":-2, "[":3,"]":-3}
        stack = []
        for alphabet in s:
            if stack and bracket_value[alphabet]<0 and stack[-1]+bracket_value[alphabet]==0:
                stack.pop()
            else:
                stack.append(bracket_value[alphabet])
        return stack == []
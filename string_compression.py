from collections import defaultdict
class Solution(object):
    def compress(self, chars):
        i,j=0,0
        while j< len(chars):
            char, length = chars[j], 1
            while j<len(chars)-1 and char==chars[j+1]:
                length,j = length+1,j+1
            chars[i] = char
            if length > 1:
                str_length = str(length)
                chars[i+1:i+1+len(str_length)] = str_length
                i+=len(str_length)
            j,i = j+1,i+1
        return i
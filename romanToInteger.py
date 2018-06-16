class Solution(object):
    def romanToInt(self, s):
        integer,subtract = 0,False
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for idx,curr in enumerate(s[:-1]):
            print idx,curr
            if roman_dict[curr] >= roman_dict[s[idx+1]] and not subtract:
                integer+=roman_dict[curr]
            elif roman_dict[curr] < roman_dict[s[idx+1]]:
                integer -= roman_dict[curr]
                subtract = False
            else:
                subtract = True
        integer+=roman_dict[s[-1]]
        return integer
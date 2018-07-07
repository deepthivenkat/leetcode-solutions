class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low,high = 0, len(letters)-1
        while low<high:
            mid = low + (high-low)//2
            if ord(letters[mid])>ord(target):
                high = mid
            else:
                low = mid+1
        
        if ord(letters[-1]) <= ord(target):
            return letters[0]
        else:
            return letters[low]
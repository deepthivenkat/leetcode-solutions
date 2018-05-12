class Solution(object):
    def thirdMax(self, nums):
        if not nums:
            return
        i,three_window,nums_len=0,[],len(nums)
        while len(set(three_window))<3 and i<nums_len:
            three_window.append(nums[i])
            i+=1
        three_window = sorted(list(set(three_window)))
        for val in nums[i:]:
            if val > three_window[0] and val < three_window[1]:
                three_window = [val]+three_window[1:]
            elif val > three_window[1] and val < three_window[2]:
                three_window = three_window[1:2] + [val] + [three_window[-1]]
            elif val> three_window[2]:
                three_window = three_window[1:]
                three_window.append(val)
        return max(nums) if len(three_window) < 3 else three_window[0]
from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        self.d = deque(maxlen=size)
        self.sum = 0
        self.size = size
        self.no_of_items = 0
        
        """
        Initialize your data structure here.
        :type size: int
        """
        

    def next(self, val):
        if self.d and self.no_of_items >= self.size:
            self.sum -= self.d.popleft()
        self.d.append(val)
        self.no_of_items += 1
        self.sum += val
        return float(self.sum)/min(self.no_of_items,self.size)
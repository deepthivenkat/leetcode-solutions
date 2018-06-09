class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_num = float("inf")
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        if not self.stack or x < self.min_num:
            self.min_num = x
        self.stack.append((x,self.min_num))
        """
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        if self.stack:
            self.stack.pop()[0]
            self.min_num= self.stack[-1][1] if self.stack else float("inf")
        """
        :rtype: void
        """
        

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        """
        :rtype: int
        """
        

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        """
        :rtype: int
        """
        v
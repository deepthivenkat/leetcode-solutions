from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        self.q2.extend([x])
        while self.q1:
            x=self.q1.popleft()
            self.q2.append(x)
        self.q1, self.q2 = self.q2, self.q1
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        if self.q1:
            return self.q1.popleft()
        
        
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        

    def top(self):
        return self.q1[0]
        """
        Get the top element.
        :rtype: int
        """
        

    def empty(self):
        return not self.q1 
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
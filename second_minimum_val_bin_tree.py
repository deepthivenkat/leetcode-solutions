class Solution(object):
    def dfs(self,node):
        if not node:
            return
        if node.val < self.min_val:
            self.min_val = node.val
        elif node.val < self.ans and node.val > self.min_val:
            self.ans = node.val
        self.dfs(node.left)
        self.dfs(node.right)
            
    def findSecondMinimumValue(self, root):
        self.min_val, self.ans = root.val,float("inf")
        self.dfs(root)
        return self.ans if self.ans!=float("inf") else -1
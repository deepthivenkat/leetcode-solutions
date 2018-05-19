class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        self.dfs(root,stack)
        return stack[k-1]
    def dfs(self,root,stack):
        if not root:
            return 
        self.dfs(root.left,stack)
        stack.append(root.val)
        self.dfs(root.right,stack)
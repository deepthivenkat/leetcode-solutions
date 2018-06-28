
class Solution(object):
    def recursive_merge(self,t1,t2):
            if t1 and t2:
                curr = TreeNode(t1.val+t2.val)
                curr.left = self.recursive_merge(t1.left,t2.left)
                curr.right = self.recursive_merge(t1.right,t2.right)
            elif t1:
                curr = TreeNode(t1.val)
                curr.left = self.recursive_merge(t1.left,None)
                curr.right = self.recursive_merge(t1.right,None)
            elif t2:
                curr = TreeNode(t2.val)
                curr.left = self.recursive_merge(None,t2.left)
                curr.right = self.recursive_merge(None,t2.right)
            else:
                return None
            
            return curr
    def mergeTrees(self, t1, t2):
        return self.recursive_merge(t1,t2)
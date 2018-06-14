import math
class Solution(object):
    def depth_cal(self,node):
        if not node:
            return [True,0]
        else:
            l_depth = self.depth_cal(node.left)
            r_depth = self.depth_cal(node.right)
            if not l_depth[0] or not r_depth[0]:
                return [False,-1]
            if abs(l_depth[1]-r_depth[1])>1:
                return [False,-1]
            return [True,1+max(l_depth[1],r_depth[1])]
    def isBalanced(self, root):
        val = self.depth_cal(root)
        return True if val[0] else False
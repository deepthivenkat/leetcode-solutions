# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        def calc_Depth(node):
            if not node:
                return 0
            else:
                return 1+ max(calc_Depth(node.left),calc_Depth(node.right))
        return calc_Depth(root)
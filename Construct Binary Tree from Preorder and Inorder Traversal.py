class Solution(object):
    def buildTree(self, preorder, inorder):
        if not inorder:
            return
        root = TreeNode(preorder.pop(0))
        in_idx = inorder.index(root.val)
        root.left = self.buildTree(preorder,inorder[:in_idx])
        root.right = self.buildTree(preorder,inorder[in_idx+1:])
        return root
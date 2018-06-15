class Solution(object):
    def trimBST(self, root, L, R):
        if not root:
            return root
        if root.val < L:
            root = self.trimBST(root.right,L,R)
        elif root.val >R:
            root = self.trimBST(root.left,L,R)
        else:
            root.right = self.trimBST(root.right,L,R)
            root.left = self.trimBST(root.left,L,R)
        return root
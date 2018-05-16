class Solution(object):
    def invertTree(self, root):
        if not root or (not root.left and not root.right):
            return root
        if root:
            left_mirror = self.invertTree(root.right) if root.right else None
            right_mirror = self.invertTree(root.left) if root.left else None
            root.left = left_mirror
            root.right = right_mirror
        return root
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if p==root or q == root:
            return root
        c = self.lowestCommonAncestor(root.left,p,q)
        d = self.lowestCommonAncestor(root.right,p,q)
        return root if c and d else c or d
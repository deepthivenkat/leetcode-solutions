class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        stack = [[root.left,root.right]]
        while stack:
            curr = stack.pop()
            lft = curr[0]
            rgt = curr[1]
            if not lft and not rgt:
                continue
            if lft and rgt and lft.val!=rgt.val or (lft and not rgt) or (rgt and not lft):
                return False
            if lft and rgt and lft.val==rgt.val:
                stack.append([lft.left,rgt.right])
                stack.append([lft.right,rgt.left])
        return True
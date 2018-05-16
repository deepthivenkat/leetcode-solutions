class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        stack = []
        def inOrder(st, parent):
            if not parent:
                return
            inOrder(st, parent.left)
            st.append(parent.val)
            inOrder(st, parent.right)
            return st
        inOrder_vals = inOrder(stack, root)
        for idx, i in enumerate(inOrder_vals[:-1]):
            if inOrder_vals[idx+1] <= i:
                return False
        return True
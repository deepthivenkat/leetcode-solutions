class Solution(object):
    def kthSmallest(self, root, k):
        stack = [root]
        while root.left:
            stack.append(root.left)
            root = root.left
        while k!=0 and stack:
            current= stack.pop()
            k-=1
            if k==0:
                return current.val
            right = current.right
            while right:
                stack.append(right)
                right = right.left
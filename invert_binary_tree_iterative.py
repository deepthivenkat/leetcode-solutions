class Solution:
    def invertTree(self, root):
        induvidual_nodes = [root]
        while induvidual_nodes:
            current = induvidual_nodes.pop()
            if current:
                current.left, current.right = current.right,current.left
                induvidual_nodes += [current.left, current.right]
        return root
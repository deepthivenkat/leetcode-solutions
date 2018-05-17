class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        if root:
            root.next = None
        cur_node_num = 0
        while root and root.left and root.right:
            root.left.next = root.right
            if cur_node_num == 0:
                    next_lvl_first_child = root.left
            if root.next:
                root.right.next = root.next.left
                root = root.next
                cur_node_num += 1
            else:
                root.right.next = None
                cur_node_num = 0
                root = next_lvl_first_child
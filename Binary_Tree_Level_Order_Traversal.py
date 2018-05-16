class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        queue = [[root]]
        processed_elements = []
        q_val = [[root.val]]
        while queue:
            current = queue[0]
            queue = queue[1:]
            processed_elements.append(current)
            current_level_nodes = []
            current_level_vals = []
            for i in current:
                if i:
                    current_level_nodes.append(i.left)
                    current_level_vals.append(i.left.val) if i.left else None
                    current_level_nodes.append(i.right)
                    current_level_vals.append(i.right.val) if i.right else None
            if current_level_nodes:
                queue.append(current_level_nodes)
                if current_level_vals:
                    q_val.append(current_level_vals)
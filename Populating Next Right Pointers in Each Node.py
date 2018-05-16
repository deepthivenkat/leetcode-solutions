class Solution:
    # @param root, a tree link node
    # @return nothing
    def levelOrder(self, root):
        if not root: return []
        queue = [[root]]
        processed_elements = []
        q_val = [[root]]
        while queue:
            current = queue[0]
            queue = queue[1:]
            processed_elements.append(current)
            current_level_nodes = []
            current_level_vals = []
            for i in current:
                if i:
                    current_level_nodes.append(i.left)
                    current_level_vals.append(i.left) if i.left else None
                    current_level_nodes.append(i.right)
                    current_level_vals.append(i.right) if i.right else None
            if current_level_nodes:
                queue.append(current_level_nodes)
                if current_level_vals:
                    q_val.append(current_level_vals)
        return q_val
    def connect(self, root):
        level_traversal = self.levelOrder(root)
        for level in level_traversal:
            level.append(None)
        for level in level_traversal:
            for idx,node in enumerate(level[:-1]):
                if node: node.next = level[idx+1]
                    
                
        
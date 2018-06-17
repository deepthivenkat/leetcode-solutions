from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        tree_str = ""
        if root:
            tree_str+=str(root.val)+"|"
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current:
                if current.left:
                    tree_str += str(current.left.val)+"|"
                else:
                    tree_str+=str(None)+"|"
                if current.right:
                    tree_str += str(current.right.val)+"|"
                else:
                    tree_str+=str(None)+"|"
                queue.extend([current.left])
                queue.extend([current.right]) 
        return tree_str
        

    def deserialize(self, data):
        
        data = data.split("|")[:-1]
        print data
        len_data = len(data)
        if not data:
            return None
        root = data[0] = TreeNode(int(data[0]))
        i,child = 0,1
        while i < len_data:
            curr = data[i]
            if curr!='None':
                if child<len_data and data[child]!='None':
                    data[child] = curr.left = TreeNode(int(data[child]))
                child+=1
                if child < len_data  and data[child]!='None':
                    data[child]=curr.right = TreeNode(int(data[child]))
                child +=1
            i+=1
        return root

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
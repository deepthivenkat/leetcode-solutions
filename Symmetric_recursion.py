class Solution(object):
    def isSymmetric(self, root):
        
        def comp(node1,node2):
            if not node1 and not node2:
                return True
            if node1 == None or node2==None:
                return False
            return node1.val==node2.val and comp(node1.left,node2.right) and comp(node1.right,node2.left)
            
        return comp(root,root)
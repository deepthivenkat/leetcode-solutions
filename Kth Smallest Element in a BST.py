class Solution(object):
    def count_nodes(self,top):
        if not top:
            return 0
        else:
            return 1+ self.count_nodes(top.left) + self.count_nodes(top.right)
        
    def kthSmallest(self, root, k):
        if root:
            num_left = self.count_nodes(root.left)
            print num_left
            if k==num_left+1:
                return root.val
            elif k <= num_left:
                return self.kthSmallest(root.left, k)
            else:
                return self.kthSmallest(root.right,k-num_left-1)
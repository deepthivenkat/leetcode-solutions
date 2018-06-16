class Solution(object):
    def findpaths(self,node,curr_path,s,result):
        if not node.left and not node.right and sum(curr_path)==s:
            return [curr_path]
        left_result,right_result = [],[]
        if node.left:
            left_result = self.findpaths(node.left,curr_path+[node.left.val],s,result)
        if node.right:
            right_result = self.findpaths(node.right,curr_path+[node.right.val],s,result)
        return left_result+right_result
    def pathSum(self, root, s):
        return self.findpaths(root,[root.val],s,[]) if root else []
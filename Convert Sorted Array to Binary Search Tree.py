class Solution(object):
    def helper(self,arr,start,end):
            if start==end:
                return None
            mid = (start+end)//2
            rt = TreeNode(arr[mid])
            rt.left, rt.right = self.helper(arr,start,mid), self.helper(arr,mid+1,end)
            return rt
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        return self.helper(nums,0,len(nums))
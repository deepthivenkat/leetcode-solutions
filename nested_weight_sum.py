
class Solution(object):
    def rec_depth_product(self,list_of,depth):
        sum_=0
        for val in list_of:
            if val.getInteger():
                sum_ += depth*val.getInteger()
            else:
                sum_+=self.rec_depth_product(val.getList(),depth+1)
        return sum_
        
    def depthSum(self, nestedList):
        return self.rec_depth_product(nestedList,1)
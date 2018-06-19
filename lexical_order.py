class Solution(object):
    def lexicalOrder(self, n):
        def dfs(res,k):
            if k<=n:
                res.append(k)
                t = 10*k
                if t<=n:
                    for i in range(10):
                        dfs(res,t+i)
                
        res=[]
        for j in range(1,10):
            dfs(res,j)
        return res
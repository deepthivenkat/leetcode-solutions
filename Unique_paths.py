class Solution(object):
    def uniquePaths(self, m, n):
        num_paths = [[0 for i in range(m)] for i in range(n)]
        for i in range(m):
            num_paths[0][i] = 1
        for i in range(n):
            num_paths[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                num_paths[j][i] = num_paths[j-1][i]+num_paths[j][i-1]
        return num_paths[n-1][m-1]
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        res = [0 for i in range(num_cols)]
        res[0]=1
        for i in range(num_rows):
            for j in range(num_cols):
                if obstacleGrid[i][j]:
                    res[j] = 0
                elif j>0:
                    res[j] += res[j-1]
        return res[num_cols-1]
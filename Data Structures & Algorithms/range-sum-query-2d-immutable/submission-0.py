class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[-1000001] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            total = 0
            for j in range(len(matrix[i])):
                total += matrix[i][j]
                self.prefix[i][j] = total
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            preRight = self.prefix[i][col2]
            preLeft = self.prefix[i][col1-1] if col1 > 0 else 0
            ans += (preRight - preLeft)
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
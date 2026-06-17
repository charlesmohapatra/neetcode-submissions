class Solution:
    def binarySortFunction(self, arr: List[int], target):
        l,r = 0, len(arr)-1
        while(l<=r):
            m = int((l+r)/2)
            if arr[m] > target:
                r = m-1
            elif arr[m] < target:
                l = m + 1
            else:
                return m
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = -1
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            if matrix[i][column - 1] >= target:
                result = self.binarySortFunction(matrix[i], target)
                if result == -1:
                    return False
                else:
                    return True
        return False
        

        
        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n
        answer = [[0] * n for i in range(m)]
        for i in range(m-1, -1 , -1):
            answer[i][n-1] = 1
            for j in range(n-2, -1, -1):
                answer[i][j] = prevRow[j] + answer[i][j+1]
            prevRow = answer[i]
            print(f"PrevRow is {prevRow}")
        print(answer)
        return answer[0][0]

        
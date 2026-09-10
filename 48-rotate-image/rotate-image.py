class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        "first lets flip by diagonal"
        temp = -1
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
                print("row col =", matrix[row][col], "col row =", matrix[col][row])

        print(matrix)

        "mirror"
        left = 0
        right = len(matrix[0])-1
        for row in range(len(matrix)):
            left = 0
            right = len(matrix[0])-1
            while(left < right):
                temp = matrix[row][left]
                matrix[row][left] = matrix[row][right]
                matrix[row][right] = temp
                left +=1
                right -= 1
        print (matrix)
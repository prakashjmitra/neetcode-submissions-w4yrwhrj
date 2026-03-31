class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bottom = ROWS - 1
        while top <= bottom:
            mid3 = (top + bottom)//2
            if target > matrix[mid3][-1]:
                top = mid3 + 1
            elif target < matrix[mid3][0]:
                bottom = mid3 - 1
            else:
                break
        if not (top <= bottom):
            return False
        mid = mid3

        l = 0
        r = len(matrix[mid]) -1
        while l <= r:
            mid2 = (l + r)//2
            print(mid2)
            if target > matrix[mid][mid2]:
                l = mid2 + 1
            elif target < matrix[mid][mid2]:
                r = mid2 - 1
            else:
                return True
        return False 
        
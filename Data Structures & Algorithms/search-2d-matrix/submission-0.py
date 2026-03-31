class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        inside = 0
        outside = len(matrix) -1
        while inside < outside:
            if matrix[inside][-1] < target:
                inside = inside + 1
            else:
                break
        mid = inside
        print(mid)
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
        
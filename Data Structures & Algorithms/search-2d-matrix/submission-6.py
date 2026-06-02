class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        counter = 0
        lc = 0
        rc = rows - 1

        while lc <= rc:
            mid = lc + (rc - lc) // 2 
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                rc = mid - 1
            else:
                lc = mid + 1
        mid = mid = lc + (rc - lc) // 2 
        print(mid)
        lc2 = 0
        rc2 = columns - 1
        while lc2 <= rc2:
            mid2 = lc2 + (rc2 - lc2) // 2
            if matrix[mid][mid2] == target:
                return True
            elif matrix[mid][mid2] > target:
                rc2 = mid2 - 1
            else:
                lc2 = mid2 + 1
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        t_row, b_row = 0, len(matrix) - 1

        while t_row < b_row:
            mid = (t_row + b_row) // 2

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target and matrix[mid][-1] > target:
                t_row = b_row = mid
            elif matrix[mid][0] > target:
                b_row = mid - 1
            else:
                t_row = mid + 1
        
        while l <= r:
            mid = (l+r)//2

            if matrix[t_row][mid] == target:
                return True
            elif matrix[t_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

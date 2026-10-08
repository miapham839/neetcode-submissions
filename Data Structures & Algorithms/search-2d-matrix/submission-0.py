class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res_row = -1
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid_row = (l + r) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                res_row = mid_row
                break
            elif target > matrix[mid_row][-1]:
                l = mid_row + 1
            elif target < matrix[mid_row][0]:
                r = mid_row - 1
        if res_row == -1:
            return False
        else:
            row = matrix[res_row]
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        

        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_top_idx = 0
        row_bottom_idx = len(matrix)-1

        while row_top_idx <= row_bottom_idx:
            mid_row_idx = row_top_idx + ((row_bottom_idx - row_top_idx) // 2)
            if target > matrix[mid_row_idx][-1]:
                row_top_idx = mid_row_idx + 1
            elif target < matrix[mid_row_idx][0]:
                row_bottom_idx = mid_row_idx - 1
            else:
                break
        
        row = (row_top_idx + row_bottom_idx) // 2
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid_idx = left + ((right - left) // 2)
            if target > matrix[row][mid_idx]:
                left = mid_idx + 1
            elif target < matrix[row][mid_idx]:
                right = mid_idx - 1
            else:
                return True

                
        return False
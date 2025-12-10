# mid - tangled, but idea was correct

class Solution:
    def get_i(self, row, column, num_columns):
        return row * num_columns + column
    
    def get_row(self, i, row_len):
        return i//row_len
    
    def get_column(self, i, row_len):
        return i%row_len

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix) # -> i
        num_columns = len(matrix[0]) # -> j
        l, r = 0, self.get_i(num_rows-1, num_columns-1, num_columns)
        while l <= r:
            mid = (l + r)//2
            if matrix[self.get_row(mid, num_columns)][self.get_column(mid, num_columns)] == target:
                return True
            elif matrix[self.get_row(mid, num_columns)][self.get_column(mid, num_columns)] < target:
                l = mid+1
            else:
                r = mid-1
        return False

        

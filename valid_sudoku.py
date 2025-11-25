# box_id = (r // 3) * 3 + (c // 3

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            seen_row = [set() for _ in range(0,9)]
            seen_column = [set() for _ in range(0,9)]
            seen_boxes = [set() for _ in range(0,9)]
            for row in range(0,9):
                for column in range(0,9):
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in seen_row[row] or board[row][column] in seen_column[column] or board[row][column] in seen_boxes[(row//3)*3+(column//3)]:
                        return False
                    seen_row[row].add(board[row][column])
                    seen_column[column].add(board[row][column]) 
                    seen_boxes[(row//3)*3+(column//3)].add(board[row][column])
            return True
            
            

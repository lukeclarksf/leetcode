class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        
        def is_valid(r, c, val):
            for i in range(9):
                if board[r][i] == val or board[i][c] == val:
                    return False
            
            start_r, start_c = 3 * (r // 3), 3 * (c // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_r + i][start_c + j] == val:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for val_char in "123456789":
                            if is_valid(r, c, val_char):
                                board[r][c] = val_char
                                if backtrack():
                                    return True
                                board[r][c] = '.'
                        return False
            return True
            
        backtrack()
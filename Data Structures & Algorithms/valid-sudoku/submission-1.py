class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen=set()
            for cell in row:
                if cell in seen:
                    return False
                elif cell ==".":
                    continue
                else:
                    seen.add(cell)
                
        for i in range(len(board)):
            seen=set()
            for j in range(len(board)):
                if board[j][i] in seen:
                    return False
                elif board[j][i]==".":
                    continue
                seen.add(board[j][i])



        for start_row in range(0,7,3):
            for start_col in range(0,7,3):
                seen=set()
                for row in range(start_row,start_row+3):
                    for col in range(start_col,start_col+3):
                        if board[row][col] in seen:
                            return False
                        elif board[row][col]==".":
                            continue
                        seen.add(board[row][col])
        return True
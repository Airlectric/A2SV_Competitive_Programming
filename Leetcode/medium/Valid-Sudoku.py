class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def rowCheck(board):
            m = len(board)
            n = len(board[0])

            for i in range(m):
                count = 0
                set_check = set()
                for j in range(n):
                    if board[i][j] != '.':
                        set_check.add(board[i][j])
                        count += 1
                if len(set_check) != count:
                    return False
            
            return True


        def columnCheck(board):
            m = len(board)
            n = len(board[0])

            for i in range(m):
                count = 0
                set_check = set()
                for j in range(n):
                    if board[j][i] != '.':
                        set_check.add(board[j][i])
                        count += 1
                if len(set_check) != count:
                    return False
            
            return True
        
        def subBoxCheck(board,b):
            count = 0
            set_check = set()
            board = [sub[b:b+3] for sub in board]
            for i in range(3):
                for j in range(3):
                    if board[i][j] != '.':
                        set_check.add(board[i][j])
                        count += 1
            if len(set_check) != count:
                return False
            
            return True
        
        def moveBoxCheck(board):
            m = len(board)
            n = len(board[0])

            for i in range(0,m,3):
                for j in range(0,n,3):
                    if subBoxCheck(board[i:i+3],j) == False:
                        return False
            
            return True

        return rowCheck(board) and columnCheck(board) and moveBoxCheck(board)
                    

        
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for i in range(len(board)):
            containMap = {}
            for k in range(len(board[i])):
                if board[i][k] != '.' and board[i][k] in containMap:
                    return False
                containMap[board[i][k]] = 1
        # check columns
        for i in range(len(board[0])):
            containMap = {}
            for k in range(len(board)):
                if board[k][i] != '.' and board[k][i] in containMap:
                    return False
                containMap[board[k][i]] = 1
        # check square
        i = 0
        while i < len(board):
            k = 0
            while k < len(board[0]):
                containMap = {}
                for x in range(3):
                    for y in range(3):
                        if board[i + x][k + y] != '.' and board[i + x][k + y] in containMap:
                            return False
                        containMap[board[x + i][k + y]] = 1
                k += 3
            i += 3
        return True
            

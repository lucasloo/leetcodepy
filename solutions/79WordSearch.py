#  Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[0]:
                return False
            if len(word) == 1 and board[x][y] == word:
                return True
            tmp = board[x][y]
            board[x][y] = None
            res = dfs(board, word[1:], x - 1, y) or dfs(board, word[1:], x + 1, y) or dfs(board, word[1:], x, y - 1) or dfs(board, word[1:], x, y + 1)
            board[x][y] = tmp
            return res
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(board, word, x, y):
                    return True
        return False

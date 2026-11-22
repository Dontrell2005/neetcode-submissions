class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
        start = [0,3,6]

        for pair in start:
            for j in start:
                sett = set()
                for i in range(pair, pair + 3):
                    for k in range(j,  j + 3):
                        if board[i][k] == '.':
                            continue
                        if board[i][k] in sett:
                            return False
                        sett.add(board[i][k])
        return True

        
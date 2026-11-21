class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
        starts = [0,3,6]
        for i in starts:
            for j in starts:
                seen = set()
        # Check the 3x3 box starting at (i, j)
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] == '.':
                            continue

                        if board[r][c] in seen:
                            return False

                        seen.add(board[r][c])
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                box = (r // 3) * 3 + c // 3
                if num in rows[r]:
                    return False
                rows[r].add(num)

                if num in cols[c]:
                    return False
                cols[c].add(num)

                if num in boxs[box]:
                    return False
                boxs[box].add(num)

            

        return True
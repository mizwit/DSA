class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, line in enumerate(board):
            h_map = {}
            for j, c in enumerate(line):

                # Check 3 X 3 boxes for duplicates
                if i % 3 == 0 and j % 3 == 0:
                    b_map = {}
                    for a in range(3):
                        for b in range(3):
                            bc = board[i + a][j + b]
                            if bc == ".": continue
                            if b_map.get(bc, None): return False
                            b_map[bc] = True
                
                # Check vertical lines for duplicates
                if i == 0:
                    v_map = {}
                    for l in board:
                        if l[j] == ".": continue
                        if v_map.get(l[j], None): return False
                        v_map[l[j]] = True

                # Check horizontal lines for duplicates
                if c == ".": continue
                if h_map.get(c, None): return False
                h_map[c] = True

        return True
    
    # Alternate Solution, removing redundant checking
    # Uses 'k' to keep track of box index
    # 'k' is calculated in two parts: 
    # 1. (i // 3) * 3 -> corresponds to 0, 3, 6
    # 2. {j // 3} -> corresponds to 0, 1, 2
    # Added together they cover all boxes -> 0 (and 1, 2), 3 (and 4, 5), 6 (and 7, 8) 

    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     rows = [set() for _ in range(9)]
    #     cols = [set() for _ in range(9)]
    #     boxs = [set() for _ in range(9)]

    #     for i in range(9):
    #         for j in range(9):
    #             cell = board[i][j]
    #             if cell == ".": continue
    #             k = ((i // 3) * 3) + (j // 3)
    #             if cell in rows[i] or cell in cols[j] or cell in boxs[k]: return False
    #             rows[i].add(cell)
    #             cols[j].add(cell)
    #             boxs[k].add(cell)
                
    #     return True
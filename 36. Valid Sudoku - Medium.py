from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = {}
        columCheck = {}
        subBoxCheck = {}
        countRow = 0
        subBox = 0
        for row in board:
            countRow += 1
            if countRow > 3:
                countRow = 1
                subBoxCheck = {}
            for idx, i in enumerate(row):
                if i != ".":
                    #row
                    rowCheck[i] = rowCheck.get(i, 0) + 1
                    if rowCheck[i] > 1:
                        return False
                    #column
                    if idx not in columCheck:
                        columCheck[idx] = []
                    if int(i) in columCheck[idx]:
                        return False
                    columCheck[idx].append(int(i))
                    #subBox
                    if idx < 3:
                        subBox = 1
                        if subBox not in subBoxCheck:
                            subBoxCheck[subBox] = []
                        if int(i) in subBoxCheck[subBox]:
                            return False
                        subBoxCheck[subBox].append(int(i))
                    elif idx > 2 and idx < 6:
                        subBox = 2
                        if subBox not in subBoxCheck:
                            subBoxCheck[subBox] = []
                        if int(i) in subBoxCheck[subBox]:
                            return False
                        subBoxCheck[subBox].append(int(i))
                    else:
                        subBox = 3
                        if subBox not in subBoxCheck:
                            subBoxCheck[subBox] = []
                        if int(i) in subBoxCheck[subBox]:
                            return False
                        subBoxCheck[subBox].append(int(i))
            rowCheck = {}
        return True
        

  
sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
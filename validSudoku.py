"""
Approach: Have a set for each row and col and the boxes whose index can be calculated using the row and col
number. 
t.c. => O(1)
s.c. => O(1)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for i in range(9)]
        colSet = [set() for i in range(9)]
        boxSet = [set() for i in range(9)]
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                #row
                if board[row][col] in rowSet[row]:
                    return False
                else:
                    rowSet[row].add(board[row][col])
                
                #column
                if board[row][col] in colSet[col]:
                    return False
                else:
                    colSet[col].add(board[row][col])
                    
                #box
                boxNum = ((row//3)*3 + (col//3))
                if board[row][col] in boxSet[boxNum]:
                    return False
                else:
                    boxSet[boxNum].add(board[row][col])          
        return True
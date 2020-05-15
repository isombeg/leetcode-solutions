class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHashMap = dict()
        colHashMap = []
        gridHashMap = []
        
        for i in range(9):
            colHashMap.append(dict())
            gridHashMap.append(dict())
        
        #Validate rows:
        for row in range(9):
            for col in range(9):
                # Check if empty
                if board[row][col] == '.':
                    continue
                
                #Validate for row
                if board[row][col] in rowHashMap:
                    return False
                else:
                    rowHashMap[board[row][col]] = True
                    
                #Validate for column
                if board[row][col] in colHashMap[col]:
                    return False
                else:
                    colHashMap[col][board[row][col]] = True
                
                #Validate for grid
                if row < 3:
                    if col < 3:
                        if board[row][col] in gridHashMap[0]:
                            return False
                        else:
                            gridHashMap[0][board[row][col]] = True
                    elif col < 6:
                        if board[row][col] in gridHashMap[1]:
                            return False
                        else:
                            gridHashMap[1][board[row][col]] = True
                    else: 
                        if board[row][col] in gridHashMap[2]:
                            return False
                        else:
                            gridHashMap[2][board[row][col]] = True
                
                elif row < 6:
                    if col < 3:
                        if board[row][col] in gridHashMap[3]:
                            return False
                        else: gridHashMap[3][board[row][col]] = True
                    elif col < 6:
                        if board[row][col] in gridHashMap[4]:
                            return False
                        else: gridHashMap[4][board[row][col]] = True
                    else: 
                        if board[row][col] in gridHashMap[5]:
                            return False
                        else: gridHashMap[5][board[row][col]] = True
                else:
                    if col < 3:
                        if board[row][col] in gridHashMap[6]:
                            return False
                        else: gridHashMap[6][board[row][col]] = True
                    elif col < 6:
                        if board[row][col] in gridHashMap[7]:
                            return False
                        else: gridHashMap[7][board[row][col]] = True
                    else: 
                        if board[row][col] in gridHashMap[8]:
                            return False
                        else: gridHashMap[8][board[row][col]] = True
            rowHashMap = dict()
        return True
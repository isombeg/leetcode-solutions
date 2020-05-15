class Solution:
    def convert(self, s: str, numRows: int) -> str:
        self._rows = []
        self._currRow = 0
        self._dir = True
        
        zigzag = ""
        
        for x in range(numRows):
            self._rows.append([])
            
        for char in s:
            self._rows[self._currRow].append(char)
            self.bounce()
            
        for row in self._rows:
            for char in row:
                zigzag += char
                
        return zigzag
        
    def bounce(self):
        if len(self._rows) == 1:
            return 0
        elif self._currRow == 0:
            self._dir = True
        elif self._currRow == len(self._rows) - 1:
            self._dir = False
            
        if self._dir:
            self._currRow += 1
        else:
            self._currRow -= 1
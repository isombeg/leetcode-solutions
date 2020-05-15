def genParen(n):
    
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    
    rslt = [] 
    a,b = [], []
    i,j = 0,n-1
    
    while not j<i:
        
        a.append(genParen(i))
        b.append(genParen(j))

        i += 1
        j -= 1
        
    for r in range(len(a)):
        for i in a[r]:
            for j in b[r]:
                rslt.append('(' + i + ')' + j)
                if not len(i) == len(j):
                    rslt.append('(' + j + ')' + i)
    
    return rslt

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return genParen(n)
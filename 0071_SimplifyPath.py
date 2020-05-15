class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = path.split("/")
        
        stack = []
        
        
        for elem in temp:
            if elem == '':
                continue
            elif elem == "..":
                if len(stack) > 0:
                    stack.pop()
            elif elem != ".":
                stack.append(elem)
                
        if len(stack) == 0:
            return '/'
        
        rslt = ''
        for elem in stack:
            rslt += '/'
            rslt += elem
            
        return rslt
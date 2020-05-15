class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = dict()
        
        while n != 1:
            if n in hashmap:
                return False
            else:
                hashmap[n] = True
                a,n = n,0
                while a != 0:
                    n += (a % 10)**2
                    a //= 10
        
        return True
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        # Special case: sequence has 10 or less nucleotides
        if len(s) <= 10:
            return []
        
        hashmap = dict()
        rslt = []
        for i in range(len(s)-9):
            if s[i:i+10] in hashmap:
                if hashmap[s[i:i+10]] == True:
                    rslt.append(s[i:i+10])
                    hashmap[s[i:i+10]] = False
                else: continue
            else:
                hashmap[s[i:i+10]] = True
        
        return rslt        
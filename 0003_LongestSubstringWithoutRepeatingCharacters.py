class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        max_len (int): stores highest substring length
        window (list[str]): stores a substring
        hashTable (dict): stores characters as keys, and their indices within s
        '''
        
        max_len = 0
        window = []
        hashTable = {}
        
        for s_index in range(len(s)):
            
            # When substring contains current character
            if s[s_index] in hashTable:
                
                # Deleting all characters which come before current character
                # in substring from the substring and hashTable
                while(window[0] != s[s_index]):
                    hashTable.pop(window[0])
                    window.pop(0)
                    
                hashTable.pop(window[0])
                window.pop(0)
                
            # Insert current character hash table and substring
            hashTable[s[s_index]] = s_index
            window.append(s[s_index])
            
            # Update max_len if necessary
            if (len(window) > max_len):
                max_len = len(window)
            
        return max_len
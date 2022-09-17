class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:                    
        res = ""
        
        # the word that has the greater length of chars
        big_word = strs[0] # we will assume that
        
        for i in range(len(big_word)): # 0, 1, 2, ...
            for word in strs:
                
                if i == len(word):
                    # that mean the current word has graete a number of chars
                    return res
                
                if word[i] != big_word[i]:
                    # that mean the prefix is changed
                    return res
                
            res += strs[0][i]
        
        return res
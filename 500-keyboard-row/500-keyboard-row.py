class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")

        for word in words:
            wordLetters = set(word.lower())
            if wordLetters <= row1 or wordLetters <= row2 or wordLetters <= row3:
                res.append(word)
                
        return res
        
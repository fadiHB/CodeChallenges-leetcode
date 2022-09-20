class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ""
        for i in digits:
            str_num += str(i)
            
        large = int(str_num) + 1
        
        res = []
        for i in str(large):
            res.append(int(i))
        
        return res
        
        
        
        
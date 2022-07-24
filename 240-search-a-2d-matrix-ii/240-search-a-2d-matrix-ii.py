class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(lst):
            l = 0
            r = len(lst)-1
            while r >= l:
                mid = (l + r) // 2
                num = lst[mid]
                if num == target:
                    return True
                elif num > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        
        
        for row in matrix:
            if binarySearch(row):
                return True 
        return False
        
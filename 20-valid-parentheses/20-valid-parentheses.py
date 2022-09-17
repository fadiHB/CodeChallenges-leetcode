class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '(': ')', '[': ']'}
        stack = [] # list of open brackets
        
        for char in s:
            if char in brackets:
                stack.append(char)
                continue
                
            # if the stack is empty (no open brackets)
            # and we are here hanlding a close bracket, so return false
            elif not stack:
                return False
            
            # Here that mean the stack is not empty, and we have a close bracket
            # so we need to check and compare
            elif  brackets[stack.pop()] != char:
                return False
            
            # If we reached here,
            # it means the closed bracket match the last open one that we already removed 
            
        return not stack
        
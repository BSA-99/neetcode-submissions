class Solution:
    def isValid(self, s: str) -> bool:
        dict_stak={')':'(', ']':'[','}':'{'}
        stack=[]

        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack or stack[-1]!=dict_stak.get(i,''):
                    return False
                stack.pop()
        return not stack
        
        
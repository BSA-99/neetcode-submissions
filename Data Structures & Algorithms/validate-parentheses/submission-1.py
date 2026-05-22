class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        dict1 = {'(':')', '{':'}', '[':']'}

        for i in s:
            if i in dict1.keys():
                stack1.append(i)
            else:
                if not stack1:
                    return False
                a=stack1.pop()
                if dict1[a] == i:
                    continue
                else:
                    return False
        return len(stack1)==0
            


        
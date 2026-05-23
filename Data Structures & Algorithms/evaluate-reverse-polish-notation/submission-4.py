class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1=[]
        oper = ["+","-","*","/"]

        for i in tokens:
            if i not in oper:
                stack1.append(int(i))
            else:
                a=stack1.pop()
                b=stack1.pop()
                if i == "+":
                    stack1.append(b+a)
                elif i == "-":
                    stack1.append(b-a)
                elif i == "*":
                    stack1.append(b*a)
                else:
                    stack1.append(int(b / a))
        return stack1[-1]

        
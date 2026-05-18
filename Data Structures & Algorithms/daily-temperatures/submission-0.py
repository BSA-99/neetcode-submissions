class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*(len(temperatures))
        stack=[]

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prevday=stack.pop()
                res[prevday]=i-prevday
            stack.append(i)
        return res



        
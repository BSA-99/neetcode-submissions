class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]*len(temperatures)
        s1=[]

        for i in range(len(temperatures)):
            while len(s1)!=0 and temperatures[i]>temperatures[s1[-1]]:
                j=s1.pop()
                results[j] = i-j
            s1.append(i)
        return results



            


        
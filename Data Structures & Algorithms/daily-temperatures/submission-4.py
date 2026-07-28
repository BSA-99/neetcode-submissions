class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while len(st)!=0 and temperatures[i]>temperatures[st[-1]]:
                j = st.pop()
                result[j] = i-j
            st.append(i)
        return result

        
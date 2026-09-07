class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        times=[]
        st =[]
        
        for pos, sp in pairs:
            time = (target-pos)/sp
            times.append(time)
        
        for i in range(len(position)):
            if len(st)==0 or times[i]>st[-1]:
                st.append(times[i])
        return len(st)
            
            
        
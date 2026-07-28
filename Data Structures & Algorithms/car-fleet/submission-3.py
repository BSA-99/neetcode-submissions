class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_fleet = list(zip(position, speed)) #[(7,1),(4,2),(1,2),(0,1)]
        new_fleet.sort(reverse=True)
        time=[]
        st = []
        for i in range(len(new_fleet)):
             time.append((target-new_fleet[i][0])/new_fleet[i][1])
        for i in range(len(time)):
            if not st or time[i]>st[-1]:
                st.append(time[i])
            else:
                continue
        return len(st)

            


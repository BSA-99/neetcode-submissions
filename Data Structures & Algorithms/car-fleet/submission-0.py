class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        times = []
        stack=[]

        for pos, sp in pairs:
            time = (target - pos)/sp
            times.append(time)

        for i in range(len(position)):
            if len(stack)==0 or times[i]>stack[-1]:
                stack.append(times[i])
            else:
                continue
        return len(stack)

            
        
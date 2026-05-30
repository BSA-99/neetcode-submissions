import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        pile = sorted(piles)

        l,r = 1, pile[-1]
        best_time = pile[-1]

        while l<=r:
            mid = (l+r)//2
            hours = 0
            for pi in pile:
                hours += math.ceil(pi/mid)
            
            if hours>h:
                l=mid+1
            else:
                best_time = mid
                r= mid-1
        return best_time


        
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles, k, h):
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)
            return hours<=h
        
        L=1
        R=max(piles)
        result = R

        while L<=R:
            mid = (L+R)//2

            if canFinish(piles, mid, h):
                result = mid
                R = mid-1
            else:
                L=mid+1
        return result


        
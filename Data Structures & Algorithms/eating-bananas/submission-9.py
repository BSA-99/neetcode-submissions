class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result=float('inf')

        while left<=right:
            mid = (left+right)//2
            total_hours = 0
            for i in piles:
                hour = math.ceil(i/mid)
                total_hours+=hour
            if total_hours <= h:
                result = mid
                right = mid-1
            else:
                left = mid+1
        return result

        
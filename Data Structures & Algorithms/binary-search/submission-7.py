class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums)-1

        while l<=r:
            mp = (l+r)//2
            if target == nums[mp]:
                return mp
            elif target > nums[mp]:
                l=mp+1
            else:
                r=mp-1
        return -1



        
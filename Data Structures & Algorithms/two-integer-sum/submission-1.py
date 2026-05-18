class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seem={}
        for i,x in enumerate(nums):
            need=target - x
            if need in seem:
                return [seem[need], i]
            seem[x]=i
        
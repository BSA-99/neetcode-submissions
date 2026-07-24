class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for index, value in enumerate(nums):
            left = target-value

            if left in hm:
                return [hm[left], index]
            else:
                hm[value] = index
            
        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ha= {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in ha:
                return [ha[diff], index]
            ha[value] = index
            
        
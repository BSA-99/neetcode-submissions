class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for index, value in enumerate(nums):
            to_find = target - value

            if to_find in hashmap:
                return [hashmap[to_find], index]
            hashmap[value] = index

            
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        is_seen = {}

        for index, val in enumerate(nums):
            to_find = target - val
            if to_find in is_seen:
                return [is_seen[to_find], index]
            is_seen[val] = index
        

        
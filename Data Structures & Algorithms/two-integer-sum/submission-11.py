class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for index, value in enumerate(nums):
            to_find = target - value

            if to_find in res:
                return [res[to_find], index]
            res[value] = index
        

            

        
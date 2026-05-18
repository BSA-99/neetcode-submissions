class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_nums = []

        for i in nums:
            if i in dup_nums:
                return True
            dup_nums.append(i)

        return False
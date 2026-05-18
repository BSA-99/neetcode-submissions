class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_dup = []
        for i in nums:
            if i in check_dup:
                return True
            check_dup.append(i)

        return False
        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        isSeen = set()

        for i in nums:
            if i in isSeen:
                return i
            else:
                isSeen.add(i)
        
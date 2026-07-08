class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr1 = []
        for i in nums:
            if i in arr1:
                return True
            arr1.append(i)
        return False
            



        

        
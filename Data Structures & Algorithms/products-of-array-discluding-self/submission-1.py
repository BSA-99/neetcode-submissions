class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                left[i] = 1
            else:
                left[i]=left[i-1]*nums[i-1]

        for j in range(len(nums)-1,-1, -1):
            if j == len(nums)-1:
                right[j] = 1
            else:
                right[j] = right[j+1]*nums[j+1]
        result = [x*y for x, y in zip(left,right)]
        return result

                




        
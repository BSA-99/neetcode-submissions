class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
            #[1,1,2,4]
        
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        results = []

        for i in range(n):
            results.append(prefix[i]*suffix[i])
        return results
        

            
        
        
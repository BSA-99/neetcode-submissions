class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_sums = sorted(nums)
        l1 = []

        for i in range(len(new_sums)):
            if i>0 and new_sums[i]==new_sums[i-1]:
                continue
            left = i+1
            right = len(new_sums)-1

            while left<right:
                if new_sums[left]+new_sums[right]+new_sums[i]==0:
                    l1.append([new_sums[left],new_sums[right],new_sums[i]])

                    while left<right and new_sums[left]==new_sums[left+1]:
                        left+=1
                    while left<right and new_sums[right]==new_sums[right-1]:
                        right-=1
                
                    left+=1
                    right-=1
                elif new_sums[left]+new_sums[right]+new_sums[i]<0:
                    left +=1
                else:
                    right -=1
        return l1
                    
                    

                        
                    
            
                

        
        
        
        
        
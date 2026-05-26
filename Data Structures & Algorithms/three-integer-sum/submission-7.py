class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums=sorted(nums)
        l1=[]

        for i in range(len(new_nums)):
            if i>0 and new_nums[i]==new_nums[i-1]:
                continue
            left = i+1
            right =  len(new_nums)-1

            while left<right:
                if new_nums[i]+new_nums[left]+new_nums[right]==0:
                    l1.append([new_nums[i], new_nums[left],new_nums[right]])

                    while left<right and new_nums[left]==new_nums[left+1]:
                        left+=1
                    while left<right and new_nums[right]==new_nums[right-1]:
                        right-=1

                    left+=1
                    right-=1
                    
                elif new_nums[i]+new_nums[left]+new_nums[right]<0:
                    left+=1
                else:
                    right-=1

        return l1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[ [] for i in range(len(nums)+1)]

        for num in nums:
            count[num]=1+count.get(num,0) #count={1:1,2:2,3:3}
        
        for num, cnts in count.items():
            freq[cnts].append(num) # freq = [0,1,2,3,0,0,0]

        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res



        
        
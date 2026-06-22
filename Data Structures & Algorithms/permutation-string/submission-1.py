class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = Counter(s1)
        window_count = Counter(s2[0:len(s1)])

        l = 0
        r = len(s1)-1

        while r<len(s2):
            if window_count == s1_count:
                return True
            if r+1 < len(s2):
                window_count[s2[l]]-=1
                window_count[s2[r+1]]+=1
            l+=1
            r+=1
        return False
            

            
                
                
            
        

        
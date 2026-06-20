class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_count = Counter(s1) #{"a":1, "b":1, "c":1}
        window = Counter(s2[0:len(s1)]) #{"l":1,"e":1,"c":1}

        l = 0
        r = len(s1)-1 #3

        while r < len(s2):
            if window == s1_count:
                return True
            if r+1 < len(s2):
                window[s2[l]]-=1 # {"l":0,"e":1,"c":1}
                window[s2[r+1]] +=1 #{"l":0,"e":1,"c":1,"a":1}
            l+=1
            r+=1
        
        return False






        

        
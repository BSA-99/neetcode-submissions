class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_freq = [0]*26

        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            s1_freq[index]+=1

        window_freq = [0]*26

        for r in range(len(s1)):
            index = ord(s2[r]) - ord('a')
            window_freq[index]+=1
        
        if window_freq == s1_freq:
            return True
        l=0
        for i in range(len(s1), len(s2)):
            index = ord(s2[i]) - ord('a')
            window_freq[index]+=1
            window_freq[ord(s2[l])-ord('a')]-=1
            l+=1
            if window_freq == s1_freq:
                return True
        return False
        







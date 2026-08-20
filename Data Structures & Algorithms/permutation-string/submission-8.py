class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l=0
        main_arr = [0]*26
        s1_arr = [0]*26
        for i in range(len(s1)):
            ind = ord(s1[i])-ord('a')
            s1_arr[ind]+=1

        for i in range(len(s1)):
            ind = ord(s2[i])-ord('a')
            main_arr[ind]+=1
        
        if main_arr == s1_arr:
            return True
        
        for r in range(len(s1), len(s2)):
            ind = ord(s2[r])-ord('a')
            main_arr[ord(s2[l])-ord('a')]-=1
            main_arr[ind]+=1
            l+=1
            if main_arr == s1_arr:
                return True
        return False


        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
            
        l=0
        arr = [0]*26
        s1_arr = [0]*26
        for i in range(len(s1)):
            index = ord(s1[i])-ord('a')
            s1_arr[index]+=1

        for r in range(len(s1)):
            index1= ord(s2[r])-ord('a')
            arr[index1]+=1
        
        if s1_arr == arr:
            return True
        
        for i in range(len(s1), len(s2)):
            index2 = ord(s2[i])-ord('a')
            arr[index2]+=1
            arr[ord(s2[l])-ord('a')]-=1
            l+=1
            if arr == s1_arr:
                return True
        return False


        
        
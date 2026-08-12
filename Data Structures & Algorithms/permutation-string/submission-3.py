class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        arr = [0]*26
        l=0
        s1_array = [0]*26

        for i in range(len(s1)):
            index = ord(s1[i])-ord('a')
            s1_array[index]+=1
            
        for r in range(len(s1)):
            index1 = ord(s2[r])-ord('a')
            arr[index1]+=1

        if s1_array == arr:
            return True

        for i in range(len(s1), len(s2)):
            index = ord(s2[i])-ord('a')
            arr[index]+=1
            arr[ord(s2[l])-ord('a')]-=1
            l+=1
            if arr == s1_array:
                return True
        return False
            
            
            
        
        
    



        
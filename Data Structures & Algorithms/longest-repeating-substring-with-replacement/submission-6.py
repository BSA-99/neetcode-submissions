class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0]*26
        max_frequency = 0
        l=0
        result = 0

        for r in range(len(s)):
            index = ord(s[r])-ord('A')
            arr[index]+=1
            max_frequency = max(max_frequency, arr[index])
            if (r-l+1)-max_frequency >k:
                arr[ord(s[l])-ord('A')]-=1
                l+=1
            Window_len=r-l+1
            result = max(result, Window_len)
        return result
            
        

        
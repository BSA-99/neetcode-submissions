class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        l=0
        max_freq = 0
        result = 0

        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            count[index]+=1
            max_freq = max(max_freq, count[index])
            if (r-l+1) - max_freq > k:
                count[(ord(s[l])-ord('A'))]-=1
                l+=1
            window_len = r-l+1
            result = max(result, window_len)
        return result

        
        
        
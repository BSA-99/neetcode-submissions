class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = [0]*26
        l=0
        max_frequency = 0
        max_len = 0

        for r in range(len(s)):
            index = ord(s[r])-ord('A')
            char[index]+=1
            max_frequency = max(max_frequency, char[index])

            if (r-l+1)-max_frequency >k:
                char[ord(s[l])-ord('A')]-=1
                l+=1
            window_len = r-l+1
            max_len = max(max_len, window_len)
        return max_len


        
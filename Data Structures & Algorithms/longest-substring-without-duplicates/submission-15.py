class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        isSeen = set()

        for i in range(len(s)):
            while s[i] in isSeen:
                isSeen.remove(s[l])
                l+=1
            isSeen.add(s[i])
            max_len = max(max_len, i-l+1)
        return max_len
            
            
                
            
        
        
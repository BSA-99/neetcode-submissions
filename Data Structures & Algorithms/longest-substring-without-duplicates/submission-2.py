class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChar = set()
        left = 0
        maaxLen = 0

        for r in range(len(s)):
            while s[r] in seenChar:
                seenChar.remove(s[left])
                left+=1
            seenChar.add(s[r])
            maaxLen = max(maaxLen, r-left +1 )

        return maaxLen

        
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen=0
        isSeen=set()

        for right in range(len(s)):
            while s[right] in isSeen:
                isSeen.remove(s[left])
                left+=1
            isSeen.add(s[right])
            maxLen = max(maxLen, right-left+1)

        return maxLen



        
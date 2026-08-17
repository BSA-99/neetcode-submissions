class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        isSeen = set()
        l=0
        sub_len = 0

        for r in range(len(s)):

            while s[r] in isSeen:
                isSeen.remove(s[l])
                l+=1
            isSeen.add(s[r])
            sub_len = max(sub_len, r-l+1)
        return sub_len


            
        
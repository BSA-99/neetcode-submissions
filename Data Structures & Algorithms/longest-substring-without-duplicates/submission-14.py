class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_len = 0
        isSeen = set()

        for r in range(len(s)):
            while s[r] in isSeen:
                isSeen.remove(s[l])
                l+=1
            isSeen.add(s[r])
            maximun_len = r-l+1
            max_len = max(max_len, maximun_len)
        return max_len
            


        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenchar = set()
        l=0
        sub_len = 0
        for r in range(len(s)):
            while s[r] in seenchar:
                seenchar.remove(s[l])
                l+=1
            seenchar.add(s[r])
            sub_len = max(sub_len, r-l+1)
        return sub_len






        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_len = 0
        dict = {}
        for i in range(len(s)):
            if s[i] in dict.keys() and dict[s[i]]>=l:
                l=dict[s[i]]+1
            dict[s[i]] = i
            max_len = max(max_len, (i-l)+1)
        return max_len





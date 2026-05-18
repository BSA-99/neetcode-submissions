class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        max_length = 0
        window = set()
        right = 0
        while right<len(s):
            if s[right] in window:
                window.remove(s[left])
                left+=1
            else:
                window.add(s[right])
                max_length = max(max_length, right-left+1)
                right+=1

        return max_length



        
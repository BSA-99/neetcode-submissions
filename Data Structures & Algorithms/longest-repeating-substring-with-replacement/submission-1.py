class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_length = 0
        count = {}

        while right<len(s):
            count[s[right]] = count.get(s[right],0)+1

            length = right-left+1
            
            if length - max(count.values()) <=k:
                max_length = max(max_length, length)
            else:
                count[s[left]] -=1
                left+=1
            right+=1
        return max_length
                







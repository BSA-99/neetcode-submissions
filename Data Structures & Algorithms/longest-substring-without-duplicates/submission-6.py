class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        max_len = 0
        seen=[]

        for i in range(len(s)):
            if s[i] not in seen:
                seen.append(s[i])
                r+=1
                
            else:
                while s[i] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.append(s[i])
            max_len = max(max_len,len(seen))

        return max_len

        
                
            

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s.lower():
            if i.isalnum():
                new_s+=i
        
        l,r = 0, len(new_s)-1

        for i in new_s:
            if new_s[l] != new_s[r]:
                return False
            l+=1
            r-=1
        return True
        
        
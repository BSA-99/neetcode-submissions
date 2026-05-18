class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i == " " or not i.isalnum():
                continue
            else:
                st+=i.lower()
        
        return st == st[::-1]

        
        
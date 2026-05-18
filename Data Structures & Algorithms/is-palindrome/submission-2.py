class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s.lower():
            if i.isalnum():
                new_str+=i
            else:
                continue
        left = 0
        right = len(new_str)-1

        while left < right:
            if new_str[left]!=new_str[right]:
                return False
            else:
                left+=1
                right-=1
        return True

            

        

        
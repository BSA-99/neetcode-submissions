class Solution:
    def isPalindrome(self, s: str) -> bool:

        news=""

        for i in s.lower():
            if i.isalnum():
                news+=i

        l,r = 0, len(news)-1
        
        while l<r:
            if news[l]!=news[r]:
                return False
            else:
                l+=1
                r-=1
        return True
    




        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0]*26
        l=0
        most_frequent = 0
        max_len = 0

        for r in range(len(s)):
            index = ord(s[r])-ord('A')
            arr[index]+=1
            most_frequent = max(most_frequent, arr[index])

            if (r-l+1)-most_frequent > k:
                arr[ord(s[l])-ord('A')]-=1
                l+=1
            max_len = max(max_len, r-l+1)
        return max_len



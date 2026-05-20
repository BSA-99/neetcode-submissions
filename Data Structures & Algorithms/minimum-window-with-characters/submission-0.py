class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for i in t:
            t_count[i] = t.count(i)
        need = len(t_count)
        have = 0
        window={}
        left = 0
        right = 0 
        res_left = 0
        res_right = float("inf")

        while right<len(s):
            window[s[right]] = window.get(s[right],0)+1
            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                have+=1
            
            while need == have:
                if right - left < res_right - res_left:
                    res_left = left
                    res_right = right

                if s[left] in t_count and window[s[left]] == t_count[s[left]]:
                    have -=1
                window[s[left]]-=1
                left+=1
            right+=1
        return s[res_left:res_right+1] if res_right!=float("inf") else ""










        
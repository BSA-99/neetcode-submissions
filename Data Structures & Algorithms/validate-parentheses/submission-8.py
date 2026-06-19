class Solution:
    def isValid(self, s: str) -> bool:

        paran = {"{":"}", "[":"]", "(":")"}
        st = []

        for i in s:
            if i in paran:
                st.append(i)
            else:
                if not st:
                    return False
                a=st.pop()
                if paran[a] == i:
                    continue
                else:
                    return False
        return len(st)==0
                    
                    
                    

        
        
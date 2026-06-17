class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {"[":"]", "(":")", "{":"}"}
        st=[]
        
        for i in s:
            if i in par_dict:
                st.append(i)
            else:
                if not st:
                    return False
                a = st.pop()
                if par_dict[a] == i:
                    continue
                else:
                    return False
        return len(st)==0
                
                
                
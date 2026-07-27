class Solution:
    def isValid(self, s: str) -> bool:
        paran_dict = {"{":"}","[":"]","(":")"}
        st=[]

        for i in s:
            if i in paran_dict:
                st.append(i)
            else:
                if not st:
                    return False
                a = st.pop()
                if paran_dict[a]==i:
                    continue
                else:
                    return False
        return len(st)==0        
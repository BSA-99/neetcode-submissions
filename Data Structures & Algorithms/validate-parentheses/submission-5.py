class Solution:
    def isValid(self, s: str) -> bool:

        ex={"[":"]", "{":"}", "(":")"}
        st=[]

        for i in s:
            if i in ex.keys():
                st.append(i)
            else:
                if not st:
                    return False
                a=st.pop()
                if ex[a]==i:
                    continue
                else:
                    return False
        return len(st)==0



        
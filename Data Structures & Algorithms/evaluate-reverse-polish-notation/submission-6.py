class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        oper = ["+","-","*","/"]
        
        for i in tokens:
            if i not in oper:
                st.append(int(i))
            else:
                a=st.pop()
                b=st.pop()

                if i=="+":
                    st.append(b+a)
                elif i=="-":
                    st.append(b-a)
                elif i=="*":
                    st.append(b*a)
                else:
                    st.append(int(b/a))
        return st[-1]



        
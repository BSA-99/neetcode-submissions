class Solution:
    def isValid(self, s: str) -> bool:
        st = {'(':')', '[':']', '{':'}'}
        stac =[]

        for i in s:
            if i in st:
                stac.append(i)
            else:
                if not stac:
                    return False
                a = stac.pop()
                if st[a]==i:
                    continue
                else:
                    return False
        return len(stac)==0
                
                    
                
                
                
                
            
        
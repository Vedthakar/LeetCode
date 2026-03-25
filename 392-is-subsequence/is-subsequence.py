class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s) == 0):
            return True
        if(len(t) == 0):
            return False
        p = 0
        tr = 0
        while(p < len(s) and tr < len(t)):
            print("inloop")
            if(s[p] == t[tr]):
                p +=1
            tr +=1
            print(p)
            
        return p == (len(s))

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_new=sorted(s)
        t_new=sorted(t)
        if s_new==t_new:
            return True
        else:
            return False

        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            
        
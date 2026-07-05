class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        '''
        s_new=sorted(s)
        t_new=sorted(t)
        if s_new==t_new:
            return True
        else:
            return False
        '''
        '''
        d={}
        e={}
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        for ch in t:
            if ch in e:
                e[ch]+=1
            else:
                e[ch]=1      
        if d==e:
            return True
        else: 
            return False      
        '''

        d={}
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch]-=1
                if d[ch]<0:
                    return False
             
        return True
            
        
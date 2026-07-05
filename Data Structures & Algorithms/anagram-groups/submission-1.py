class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        d={}
        for i in strs:
            k="".join(sorted(i))
            if k in d:
                d[k].append(i)
            else:
                d[k]=[i]
        return list((d.values()))
        '''
        d={}
        for word in strs:
            freq=26*[0]
            for ch in word:
                freq[ord(ch)-ord('a')]+=1
            key=tuple(freq)
            if key in d:
                d[key].append(word)
            else:
                d[key]=[word]
        return list(d.values())



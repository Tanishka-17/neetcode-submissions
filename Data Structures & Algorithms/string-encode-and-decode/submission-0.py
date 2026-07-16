class Solution:
    # can't use seperators, think why what if i use a $ and there's also
    # a $ in the original list??

    def encode(self, strs: List[str]) -> str:
        enocded_string=""
        for s in strs:
            enocded_string+=str(len(s))+"#"+ s
        return enocded_string
    def decode(self, s: str) -> List[str]:
        temp=""
        current=""
        decoded_strs=[]
        i=0
        while i < len(s):
            while s[i]!="#":
                temp+=s[i]
                i+=1
                # pointer has stopped at # since condn is false
                #and stopped 
            length=int(temp)
            i+=1
            for j in range(length):
                current+=s[i]
                i+=1
            decoded_strs.append(current)
            current=""
            temp=""

        return decoded_strs    


                    
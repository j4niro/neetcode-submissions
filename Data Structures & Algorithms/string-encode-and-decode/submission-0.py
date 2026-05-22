class Solution:
    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        encoded_string = "".join(strs)
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            res.append(word)
            i = j+1+length
        return res
        
        

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        sizes = ""
        for s in strs:
            sizes+=str(len(s))+","
            res+=s
        return sizes+"#"+res     

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        sizes = []
        res = []
        i = 0
        j = 0
        while i<len(s):
            if s[i]==",":
                sizes.append(int(s[j:i]))
                j=i+1
            if s[i]=="#":
                break
            i+=1
        i+=1
        for num in sizes:
            res.append(s[i:i+num])
            i = i+num
        return res



            
        







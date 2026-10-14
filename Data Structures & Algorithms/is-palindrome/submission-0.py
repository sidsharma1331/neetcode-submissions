class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for i in range(len(s)):
            if s[i].isalnum():
                p+=s[i].lower()
        i=0
        j=len(p)-1
        print(p)
        while i<j:
            if p[i]!=p[j]:
                return False
            i+=1
            j-=1
        return True        
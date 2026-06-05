import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        txt = re.sub(r'[^a-z0-9]', '', s.lower())
        pal = txt[::-1]

        if pal == txt:
            return True
        else :
            return False
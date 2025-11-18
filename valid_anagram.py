class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        if len(s) != len(t):
            return False
        for i in range(0,len(s)):
            chars[s[i]] = chars.get(s[i],0) + 1
        for j in range(0,len(s)):
            if t[j] not in chars:
                return False
            chars[t[j]] -= 1
        for k in chars.keys():
            if chars[k] != 0:
                return False
        return True
        

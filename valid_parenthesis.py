class Solution:
    def isValid(self, s: str) -> bool:
        # "([{]})"
        lookup = {"(":")", "[":"]","{":"}"}
        stack = []
        for i in range(0,len(s)):
            if s[i] in lookup:
                stack.append(s[i])
            else:
                if not stack or lookup[stack.pop()] != s[i]:
                    return False
        return not stack

        

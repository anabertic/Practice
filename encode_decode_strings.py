class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(0,len(strs)):
            s+=str(len(strs[i]))
            s+=":"
            s+=strs[i]
        return s
        

    def decode(self, s: str) -> List[str]:
        result, c = [], 0
        while c < len(s): # 0 < 7
            delimiter_str = "" # ""
            while s[c] != ":": # 
                delimiter_str += s[c] #1
                c+=1
            c+=1 #c = 2
            delimiter = int(delimiter_str) # 1
            result_str = s[c:c+delimiter]
            result.append(result_str)
            c+=delimiter
        return result

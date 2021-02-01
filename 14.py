class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # for 
        # character = strs[0]
        lcp = ""
        if len(strs) == 0:
            return ""
        minLength = 1000
        for i in range(len(strs)):
            minLength = min(minLength, len(strs[i]))
            continue
        if minLength == 0:
            return ""
        for i in range(minLength):
            status = True
            character = strs[0][i]
            for j in range(len(strs)):
                if(strs[j][i] == character):
                    continue
                else:
                    status = False
                    break
                continue
            if status:
                lcp += character
            else:
                break
        return lcp
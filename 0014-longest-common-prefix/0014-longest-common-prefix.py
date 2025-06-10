class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or strs[0][i] != j[i]:
                    return result
            result += strs[0][i]
        
        return result
            
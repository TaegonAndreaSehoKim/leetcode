class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        counted = False
        i = len(s) - 1
        if i == 0 and s[i] != ' ':
            return 1
        while i >= 0:            
            if s[i] == ' ':
                if counted == True:
                    return count
                i -= 1
            else:
                counted = True
                count += 1
                i -= 1
        return count

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        cycle_len = 2 * numRows - 2
        
        for i in range(len(s)):
            index = i % cycle_len
            
            if index < numRows:
                rows[index].append(s[i])
            else:
                rows[cycle_len - index].append(s[i])
        
        result = ""
        for row in rows:
            result += "".join(row)
            
        return result
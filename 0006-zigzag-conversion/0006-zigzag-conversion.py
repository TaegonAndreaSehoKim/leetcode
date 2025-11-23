class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = ["" for _ in range(numRows)]
        cur_row = 0
        step = 1

        for char in s:
            rows[cur_row] += char
            if cur_row == 0:
                step = 1
            elif cur_row == numRows - 1:
                step = -1
            
            cur_row += step
        
        result = ""
        for row in rows:
            result += row
        return result
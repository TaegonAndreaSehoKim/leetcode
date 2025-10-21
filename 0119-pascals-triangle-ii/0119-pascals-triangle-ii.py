class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = []
        depth = 1
        while depth <= rowIndex + 1:
            row = []
            for i in range(depth):
                if i == 0 or i == (depth - 1):
                    row.append(1)
                else:
                    previous = rows[-1]
                    newValue = previous[i - 1] + previous[i]
                    row.append(newValue)
            rows.append(row)
            depth += 1
        
        return rows[-1]
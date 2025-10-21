class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        previous = []
        depth = 1
        while depth <= rowIndex + 1:
            newRow = []
            for i in range(depth):
                if i == 0 or i == (depth - 1):
                    newRow.append(1)
                else:
                    newValue = previous[i - 1] + previous[i]
                    newRow.append(newValue)
            previous = newRow
            depth += 1            
        
        return newRow
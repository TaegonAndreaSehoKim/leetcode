class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        depth = 1
        while depth <= numRows:
            currentRow = []
            for i in range(depth):
                if i == 0 or i == (depth - 1):
                    currentRow.append(1)
                else:
                    previousRow = result[-1]
                    newValue = previousRow[i-1] + previousRow[i]
                    currentRow.append(newValue)
            result.append(currentRow)

            depth += 1
        
        return result

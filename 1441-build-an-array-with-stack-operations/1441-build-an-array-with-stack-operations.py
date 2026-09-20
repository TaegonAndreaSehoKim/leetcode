class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        index = 1
        for t in target:
            while index < t:
                result.append("Push")
                result.append("Pop")
                index += 1

            result.append("Push")
            index += 1
        return result
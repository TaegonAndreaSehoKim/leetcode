class Solution:
    
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        if people[-1] + people[-2] <= limit:
            return (len(people) + 1) // 2

        boats = 0
        left = 0
        right = len(people) - 1
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        
        return boats

class Solution:
    
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        
        if len(people) >= 2 and people[-1] + people[-2] <= limit:
            return (len(people) + 1) // 2
        
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        
        return boats

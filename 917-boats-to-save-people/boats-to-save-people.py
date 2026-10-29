class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boat = 0
        n = len(people)
        people.sort()
        left = 0
        right = n-1
        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
            right-=1
            boat+=1
        return boat




        
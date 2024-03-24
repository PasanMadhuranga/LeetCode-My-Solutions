class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        steps = 0
        curCapacity = capacity
        for i in range(n):
            if (curCapacity >= plants[i]):
                curCapacity -= plants[i]
                steps += 1
            else:
                steps += 2*i + 1
                curCapacity = capacity - plants[i]
        
        return steps


# Another solution found in the discussion section
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        steps = 0
        curCapacity = capacity
        for i in range(n):
            if (curCapacity < plants[i]):
                steps += 2*i
                curCapacity = capacity
            curCapacity -= plants[i]
        
        return steps + n

        
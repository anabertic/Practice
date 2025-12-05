class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position,speed)]
        cars.sort(reverse=True)
        stack = []
        result = 0
        for i in range(0,len(cars)):
            cars[i] = (target-cars[i][0])/cars[i][1]
            if not stack or stack[-1] < cars[i]:
                stack.append(cars[i])
                result+=1
        return result

# t = s/v
# if the car's time is lower then the one on top of stack, it's not a new fleet. If it's slower, it's a new fleet.


        

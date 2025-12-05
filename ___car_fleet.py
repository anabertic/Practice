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



        

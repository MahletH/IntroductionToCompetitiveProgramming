class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:  
        distinct_cars={}
        for i,num in enumerate(position):
            if num in distinct_cars:
                if distinct_cars[num][0]<speed[i]:
                    time=(target-num)/speed[i]
                    distinct_cars[num]=speed[i],time
            else:
                time=(target-num)/speed[i]
                distinct_cars[num]=speed[i],time
        car_fleet=0
        cur_max=float('-inf')
        for car in reversed(sorted(distinct_cars.keys())):
            if distinct_cars[car][1]>cur_max:
                car_fleet+=1
                cur_max=distinct_cars[car][1]
        return car_fleet
            
            

#!/usr/bin/env python3

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x:x[0], reverse = True)

        slowest_fleet_time = (target - cars[0][0])/cars[0][1]
        fleets = len(cars)

        for x, v in cars[1:]:

            t = (target - x)/v
            if t > slowest_fleet_time:
                slowest_fleet_time = t

            else:
                fleets -= 1

        return fleets


    def cafFleetPreferred(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x:x[0], reverse = True)

        fleets = []

        for x, v in cars:

            t = (target - x)/v
            fleets.append(t)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
            
        return len(fleets)
                

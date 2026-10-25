from typing import NamedTuple

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list([Car(speed=s, position=p) for p, s in zip(position, speed)])
        cars.sort(key=lambda c: c.position, reverse=True)
        next_fleet = cars[0]
        fleets_count = 1
        for car in cars[1:]:
            fleet_time = (target - next_fleet.position) / next_fleet.speed
            car_time = (target - car.position) / car.speed
            if car_time > fleet_time:
                fleets_count += 1
                next_fleet = car
        return fleets_count

class Car(NamedTuple):
    speed: int
    position: int
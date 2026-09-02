class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        fleets = 1
        # (distance between target and position) / speed
        # take it for the car closest to the end because it's guaranteed not to be passed
        prev_time = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            curr_car = cars[i]
            # this is how long the current car will take to get to the target
            curr_time = (target - curr_car[0]) / curr_car[1]
            # We know that if the time is less than or equal it'll be part of the same fleet
            # thus, if the time is greater than, it creates a new fleet and prev_time
            # marks the new "benchmark" to be slower than if you want to make a new fleet
            if curr_time > prev_time:
                fleets += 1
                prev_time = curr_time

        return fleets

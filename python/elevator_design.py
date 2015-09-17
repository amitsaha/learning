'''
Simple implementation of a elevator design
'''

from collections import deque

class State:

    maintenance = -99
    stationary = 0
    up = 1
    down = -1

class Elevator:

    def __init__(self, id, current_state, floor):
        self.id = id
        self.current_state = State.stationary
        self.floor = 0
        # queue of requests
        self.requests = deque()

    def move(self):
        from_floor, to_floor = self.requests.pop()
        cur_floor = self.floor
        self.current_state = State.up if from_floor < to_floor else State.down
        self.floor = to_floor
        print 'Elevator %d Moving from %d to %d' % (self.id, cur_floor, self.floor)
        self.current_state = State.stationary

class ElevatorController:

    def __init__(self, elevators):
        self.elevators = elevators

    def schedule_elevator(self, from_floor, to_floor):
        for e in self.elevators:
            if e.current_state == State.stationary and e.floor == from_floor:
                e.requests.appendleft((from_floor, to_floor))
                e.move()
                return
            if e.current_state == State.up:
                if e.floor < from_floor:
                    e.requests.appendleft((from_floor, to_floor))
                    e.move()
                    return
            if e.current_state == State.down:
                if e.floor > from_floor:
                    e.requests.appendleft((from_floor, to_floor))
                    e.move()
                    return
        # choose the stationary elevator closest to the from_floor
        ordered_elevators = sorted(self.elevators, key = lambda x:abs(x.floor-from_floor))
        e = ordered_elevators[0]
        e.requests.appendleft((from_floor, to_floor))
        e.move()

        return

# initialize for 5 elevators
ec = ElevatorController([Elevator(i, State.stationary, 0) for i in range(5)])

while True:
    from_floor = input('Enter from floor: ')
    to_floor = input('Enter to floor: ')
    ec.schedule_elevator(from_floor, to_floor)

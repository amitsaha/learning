'''
Simple parking lot design
'''

class Preference:

    regular = 'regular'
    compact = 'compat'
    handicapped = 'handicapped'

class ParkingSpotState:

    empty = 0
    occupied = 1
    
class Car:

    def __init__(self, plate, in_time, out_time, preference, parking_lot=None):
        self.plate = plate
        self.in_time = in_time
        self.out_time = out_time
        self.preference = preference
        self.parking_lot = parking_lot
        

class ParkingSpot:

    def __init__(self, type, state):
        self.type = type
        self.state = state
        
class ParkingLot:

    def __init__(self, parking_spots=[]):
        self.parking_spots = parking_spots

    def add(self, parking_spot):
        self.parking_spots.append(parking_spot)

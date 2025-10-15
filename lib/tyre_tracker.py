from datetime import datetime
class TyreTracker():
    def __init__(self):
        self.tyres = {}
        # creates/initialises empty dictionary

    def add_tyre(self, position_in_car):
        self.tyres[position_in_car] = []
    
        # adds a tyre by a given car position (as a key) 
        # with empty list of readings
    def list_tyres(self):
        return list(self.tyres.keys())
    
    def record_reading(self, position_in_car, pressure, tread_depth):
        reading = {"pressure": pressure, "tread_depth": tread_depth, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        self.tyres[position_in_car].append(reading)
        # adds a reading of pressure and tread_depth and timestamp against the position_in_car

    def get_latest_reading(self, position_of_tyre):
        reading = self.tyres[position_of_tyre]
        return reading[-1]
        
        # returns latest reading for tyre based on its position
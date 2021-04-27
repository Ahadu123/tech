class vehicle:
    def __init__(self):
        self.color = "Green"
        self.max_speed = 200
        self.current_speed = 0
    def go(self,speed):
        self.current_speed = speed
    def emergency_stop(self):
        self.current_speed = 0
    def get_out_of_car(self):
        self.current_speed = 0

class room:
    length:0.0
    breadth:0.0
    #method to calculate area 
    def calculate_area(self):
        print("area of room =",self.length*self.breadth)
        study_room=room()
        study_room.length=42.5
        study_room.breadth=30.8
        #access method
        study_room.calculate_area()
        
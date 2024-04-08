#create an object with lab and providng the using the initmethod provide upto initial value 100 and 150 and print the area of function 
class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        return self.length * self.breadth

lab = Room()
lab.length = 100
lab.breadth = 150

lab_area = lab.calculate_area()
print("Area of your lab:", lab_area)
print("Area occupied by the lab:", lab_area, "square units")
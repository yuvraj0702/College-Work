#create a class of a complex number were in two complex numbers are created with some initial values from the user define a method that can display value of those complex number inside the class 

class ComplexNumber:
    def _init_(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def display(self):
        print(f"{self.real} + {self.imaginary}i")
Rpart1 = float(input("Enter the real part of first complex number: "))
Ipart1 = float(input("Enter the imaginary part of first complex number: "))
Cnumber1 = ComplexNumber(Rpart1, Ipart1)

Rpart2 = float(input("Enter the real part of second complex number: "))
Ipart2 = float(input("Enter the imaginary part of second complex number: "))
Cnumber2 = ComplexNumber(Rpart2, Ipart2)

 
print("First complex number:")
Cnumber1.display()

print("Second complex number:")
Cnumber2.display()
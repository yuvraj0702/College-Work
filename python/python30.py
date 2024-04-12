#write a python script differentiating the default and non parametric type constructerand parametrirized
class MyClassDefault:
    def _init_(self):
        self.my_variable = 10

class MyClassParametrized:
    def _init_(self, value):
        self.my_variable = value

class MyClassNonParametric:
    def _init_(self):
        self.my_variable = None

# Default Constructor
obj_default = MyClassDefault()
print("Default Constructor - my_variable:", obj_default.my_variable)

# Parameterized Constructor
obj_parametrized = MyClassParametrized(20)
print("Parameterized Constructor - my_variable:", obj_parametrized.my_variable)

# Non-Parametric Constructor
obj_non_parametric = MyClassNonParametric()
print("Non-Parametric Constructor - my_variable:", obj_non_parametric.my_variable)
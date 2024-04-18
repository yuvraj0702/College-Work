class Vehicle:
    def _init_(self, type, manu):
        self.type = type
        self.manu = manu

    def display(self):
         print("type:", self.type)
         print("manufacturer:", self.manu)


class _4wheeler(Vehicle):
    def _init_(self, type, manu, category):
        super()._init_(type, manu)
        self.category = category


class Hyundai(_4wheeler):
    def _init_(self, type, manu, category, model):
        super()._init_(type, manu, category)
        self.model = model

    def display(self):
        super().display()
        print("category:", self.category)
        print("model:", self.model)


# Example Usage:
car = Hyundai("SUV", "Hyundai", "Utility", "Tucson")
car.display()
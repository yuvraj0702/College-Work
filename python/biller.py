from menu import menu  # Assuming menu is a dictionary containing item-price mappings
from converter import csv_to_pdf

class BillGenerator:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.bill_filename = f"{customer_name}_bill.csv"
        self.pdf_filename = f"{customer_name}_bill.pdf"
        self.prices = []

    def add_item(self, item):
        price = menu.get(item)
        if price is None:
            print("Invalid item, please try again.")
            return
        self.prices.append(price)

    def calculate_discounted_total(self, discount_percent):
        total = sum(self.prices)
        return self.apply_discount(total, discount_percent)

    @staticmethod
    def apply_discount(amount, percent):
        return amount * (1 - percent / 100)

    def generate_bill(self, discount_percent):
        with open(self.bill_filename, "w") as file:
            for item, price in menu.items():
                file.write(f"{item},{price}\n")
            file.write(f"\nDISCOUNT,{discount_percent}%")
            discounted_total = self.calculate_discounted_total(discount_percent)
            file.write(f"\nTOTAL,{discounted_total}")
        csv_to_pdf(self.bill_filename, self.pdf_filename)

def main():
    name = input("Enter customer name: ")
    discount_percent = int(input("Discount percent: "))
    bill_generator = BillGenerator(name)

    while True:
        item = input("Item (leave blank to finish): ").upper()
        if not item:
            break
        bill_generator.add_item(item)

    bill_generator.generate_bill(discount_percent)

if __name__ == "__main__":
    main()

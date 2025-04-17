import csv
from datetime import datetime
from item import Item

class POS:
    def __init__(self):
        self.basket = []
        self.bills = {}

    def add_to_basket(self, item_code, internal_price, discount, sale_price, quantity):
        try:
            item = Item(item_code, internal_price, discount, sale_price, quantity)
            self.basket.append(item)
            return f"DM Sugar Crafts: Added {item_code} | Line Total: {item.line_total}"
        except ValueError:
            return "DM Sugar Crafts: Invalid input. Prices and quantity must be numbers."

    def display_basket(self):
        if not self.basket:
            return "DM Sugar Crafts: Basket is empty."
        output = []
        for i, item in enumerate(self.basket, 1):
            output.append(f"{i}. {item.item_code} | Sale Price: {item.sale_price} | Qty: {item.quantity} | Total: {item.line_total}")
        return "\n".join(output)

    def delete_item(self, line_number):
        if 1 <= line_number <= len(self.basket):
            deleted = self.basket.pop(line_number - 1)
            return f"DM Sugar Crafts: Deleted {deleted.item_code}"
        return "DM Sugar Crafts: Invalid line number."

    def update_item(self, line_number, sale_price=None, discount=None, quantity=None):
        if 1 <= line_number <= len(self.basket):
            item = self.basket[line_number - 1]
            try:
                if sale_price:
                    item.sale_price = float(sale_price)
                if discount:
                    item.discount = float(discount)
                if quantity:
                    item.quantity = int(quantity)
                item.line_total = item.sale_price * item.quantity
                return f"DM Sugar Crafts: Updated {item.item_code}"
            except ValueError:
                return "DM Sugar Crafts: Invalid input. Prices and quantity must be numbers."
        return "DM Sugar Crafts: Invalid line number."

    def generate_bill(self):
        if not self.basket:
            return "DM Sugar Crafts: Basket is empty. Cannot generate bill.", None
        bill_number = f"DMSUGAR_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        grand_total = sum(item.line_total for item in self.basket)
        self.bills[bill_number] = self.basket[:]
        self.basket = []
        return f"DM Sugar Crafts: Bill {bill_number} Generated | Grand Total: {grand_total}", bill_number

    def search_bill(self, bill_number):
        if bill_number in self.bills:
            output = [f"DM Sugar Crafts: Bill {bill_number}:"]
            for item in self.bills[bill_number]:
                output.append(f"{item.item_code} | Total: {item.line_total}")
            return "\n".join(output)
        return "DM Sugar Crafts: Bill not found."

    def generate_tax_file(self, bill_number):
        if bill_number not in self.bills:
            return "DM Sugar Crafts: Bill not found."
        filename = f"dmsugar_tax_{bill_number}.csv"
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["item_code", "internal_price", "discount", "sale_price", "quantity", "checksum"])
                for item in self.bills[bill_number]:
                    line = f"{item.item_code},{item.internal_price},{item.discount},{item.sale_price},{item.quantity}"
                    checksum = self.calculate_checksum(line)
                    writer.writerow([item.item_code, item.internal_price, item.discount, item.sale_price, item.quantity, checksum])
            return f"DM Sugar Crafts: Tax file generated: {filename}"
        except Exception as e:
            return f"DM Sugar Crafts: Error generating tax file: {e}"

    @staticmethod
    def calculate_checksum(line):
        upper = sum(1 for c in line if c.isupper())
        lower = sum(1 for c in line if c.islower())
        digits = sum(1 for c in line if c.isdigit())
        return upper + lower + digits
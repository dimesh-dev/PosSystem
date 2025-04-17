class Item:
    def __init__(self, item_code, internal_price, discount, sale_price, quantity):
        self.item_code = item_code
        self.internal_price = float(internal_price)
        self.discount = float(discount)
        self.sale_price = float(sale_price)
        self.quantity = int(quantity)
        self.line_total = self.sale_price * self.quantity
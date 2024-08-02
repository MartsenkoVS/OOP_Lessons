class Order():
    _total_orders = 0
    _total_price = 0
    
    def __init__(self, id: int, products: list):
        self.id = id
        self.products = products
        Order._total_orders += 1
        Order._total_price += self.order_price()
    
    @classmethod
    def total_orders(cls):
        return cls._total_orders
    
    def order_price(self):
        return sum(product.price for product in self.products)
    
    @classmethod
    def total_price(cls):
        return cls._total_price
    
    def __str__(self):
        return f'Заказ: (Номер заказа={self.id}, Цена заказа={self.order_price()})'
    

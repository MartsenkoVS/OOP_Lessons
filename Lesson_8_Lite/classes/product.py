class Product():
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __eq__(self, other):
        return self.price == other.price
    
    def __lt__(self, other):
        return self.price < other.price
    
    def __str__(self):
        return f'Продукт: (Название товара={self.name}, Цена товара={self.price})'
class Customer():
    def __init__(self, name: str, orders: list):
        self.name = name
        self.orders = orders
        
    def __str__(self):
        return f'Данные клиента: (Имя={self.name})'
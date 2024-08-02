class Discount():
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent
    
    @staticmethod
    def calculate_discounted_price(price: float, discount_percent: float):
        return price * (1 - discount_percent / 100)
    
    def __str__(self):
        return f'Скидка: (Описание={self.description}, Процент={self.discount_percent})'
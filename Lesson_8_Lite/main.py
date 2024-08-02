from classes.customer import Customer
from classes.discount import Discount
from classes.order import Order
from classes.product import Product

# Создаем продукты
product_1 = Product('pen', 100)
product_2 = Product('bicycle', 20000)
product_3 = Product('mobile phone', 65000)
product_4 = Product('map', 500)

# Создаем заказы
order_1 = Order(1, [product_1, product_3])
order_2 = Order(2, [product_2])
order_3 = Order(3, [product_1, product_4])
order_4 = Order(4, [product_3])

# Создаем клиентов, добавляем им заказы
customer_1 = Customer('Ivan', [order_1])
customer_2 = Customer('Anton', [order_2, order_3])
customer_3 = Customer('Tatyana', [order_3, order_4])

# Выводим информацию о продуктах:
print(product_1)
print(product_2)
print(product_3)
print(product_4)

# Выводим информацию о заказах:
print(order_1)
print(order_2)
print(order_3)
print(order_4)

#Выводим информацию о клиентах:
print(customer_1)
print(customer_2)
print(customer_3)

# Рассчитываем количество и сумму заказов
print(f'Всего заказов: {Order.total_orders()}')
print(f'Общая сумма всех заказов: {Order.total_price()}')

# Cоздаем скидки
discount_1 = Discount('Скидка по промокоду', 5)
discount_2 = Discount('Скидка в день рождения', 10)
discount_3 = Discount('Сезонная скидка', 25)

# Выводим информацию о скидках:
print(discount_1)
print(discount_2)
print(discount_3)

# Применяем скидки к заказам
discounted_price_1 = Discount.calculate_discounted_price(order_1.order_price(), discount_1.discount_percent)
print(f'Цена заказа № {order_1.id} с учетом скидки "{discount_1.description}": {discounted_price_1}')

discounted_price_2 = Discount.calculate_discounted_price(order_2.order_price(), discount_2.discount_percent)
print(f'Цена заказа № {order_2.id} с учетом скидки "{discount_2.description}": {discounted_price_2}')

discounted_price_3 = Discount.calculate_discounted_price(order_3.order_price(), discount_3.discount_percent)
print(f'Цена заказа № {order_3.id} с учетом скидки "{discount_3.description}": {discounted_price_3}')

# Сравнение товаров по цене
if product_1 == product_2:
    print(f'Цены продуктов {product_1.name} и {product_2.name} равны')
elif product_1 > product_2:
    print(f'Продукт {product_1.name} дороже чем {product_2.name}')
else:
    print(f'Продукт {product_2.name} дороже чем {product_1.name}')
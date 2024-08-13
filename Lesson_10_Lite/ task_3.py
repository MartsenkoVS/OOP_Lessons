from classes.negative_number_error import Negative_Number_Exception

def check_positive_number(number: int | float):
    if number < 0:
        raise Negative_Number_Exception(number)
    else:
        print(f'Число положительное: {number}')
        

check_positive_number(10)
print()
check_positive_number(-10)
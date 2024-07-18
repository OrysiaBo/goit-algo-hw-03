import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка коректності вхідних параметрів
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    # Генерація унікальних випадкових чисел
    numbers_set = set()
    while len(numbers_set) < quantity:
        number = random.randint(min, max)
        numbers_set.add(number)
    
    # Перетворення множини у відсортований список
    numbers_list = sorted(numbers_set)
    
    return numbers_list

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
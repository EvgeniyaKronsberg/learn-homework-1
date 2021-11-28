"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):

    flag = 0    # переменная-флаг для выхода из программы, если какой-то из аргуметов некорректный
    
    # проверяем исключения для цены
    try:
        price = float(price)
        price = abs(price)
    except (TypeError, ValueError):
        print('Цена была введена некорректно.')
        flag = 1

    # проверяем исключения для скидки   
    try:
        discount = float(discount)
        discount = abs(discount)       
    except (TypeError, ValueError):
        print('Скидка была введена некорректно.')
        flag = 1

    # проверяем исключения для максимальной скидки
    try: 
        max_discount = int(max_discount)
        max_discount = abs(max_discount)    
    except (TypeError, ValueError):
        print('Максимальная скидка была введена некорректно.')
        flag = 1

    # если какое-то из исключений сработало, выходим
    if flag == 1:
        quit()
    # расчет цены со скидкой
    else:
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)



if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))


"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(string_1, string_2):

    #Проверка, являются ли введенные строки числом
    if type(string_1) != str and type(string_2) != str:
        return 0
    else:
        #Проверка, одинаковые ли строки
        if string_1 == string_2:
            return 1
        #Проверка, что строки разные и первая длиннее
        elif len(string_1) > len(string_2):
            return 2
        #Проверка, что вторая строка 'learn'
        elif string_2 == 'learn':
            return 3
        
    
if __name__ == "__main__":
    string_1 = input("Введите первую строку: ")
    string_2 = input("Введите вторую строку: ")

    print(main(string_1, string_2))
    
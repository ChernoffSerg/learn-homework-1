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
def cmp_str(str1, str2):
  if not (isinstance(str1, str) and isinstance(str2, str)):
    return 0
  elif str1 == str2:
    return 1
  elif str2 == 'learn':
    return 3
  elif len(str1) > len(str2):
    return 2
  else:
    return -1

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    result = cmp_str(1, 2)
    print(result)

    result = cmp_str("df", "df")
    print(result)
    
    result = cmp_str("df", "learn")
    print(result)

    result = cmp_str("df", "learn1")
    print(result)

    result = cmp_str("learn1", "df")
    print(result)

if __name__ == "__main__":
    main()

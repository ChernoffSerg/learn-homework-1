"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

scores_school = [
                {'school_class': '4a', 'scores': [3,4,4,5,2,5,3]},
                {'school_class': '10ы', 'scores': [3,2,4,3,2]},
                ]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sum_scholl = 0
    count_scores = 0
    for school_class in scores_school:
      sum_class = 0
      for scores_class in school_class["scores"]:
        sum_scholl += scores_class
        sum_class += scores_class
      scores_avg = sum_class / len(school_class["scores"])
      count_scores += len(school_class["scores"])
      num_class = school_class["school_class"]
      print(f"Средняя оценка в классе {num_class}: {scores_avg}")

    scores_avg_school = sum_scholl / count_scores
    print(f"Средняя оценка по школе:  {scores_avg_school}")
    

if __name__ == "__main__":
  main()

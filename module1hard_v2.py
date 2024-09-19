#  Вариант решения №1 - без использования циклов:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2])
                  / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
students_list_sorted = sorted(students)
list_averages = dict(zip(students_list_sorted, average_grades))
print("Вариант решения 1:", list_averages)

#  Вариант решения №2 - с использованием циклов:
grades2 = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students2 = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades2 = []
for n in grades2:
    a = sum(n) / len(n)
    average_grades2.append(a)
students_list_sorted2 = sorted(students2)
list_averages2 = {students_list_sorted2[i]: average_grades2[i] for i in range(len(students_list_sorted2))}
print("Вариант решения 2:", list_averages2)
#  Вариант решения №1 - без использования циклов. Хотя в задании указано, что создавать словари вручную
#  не нужно, у меня без использования циклов по другому не получается
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2])
                  / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
students_list = list(students)
students_list_sorted = sorted(students_list)
list_averages = {students_list_sorted[0]:average_grades[0], students_list_sorted[1]:average_grades[1],
                 students_list_sorted[2]:average_grades[2], students_list_sorted[3]:average_grades[3],
                 students_list_sorted[4]:average_grades[4]}
print("Вариант решения 1:", list_averages)

#  Вариант решения №2 - с использованием циклов:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades2 = [sum(i)/len(i) for i in grades]
students_list = list(students)
students_list_sorted = sorted(students_list)
list_averages2 = {students_list_sorted[i]:average_grades2[i] for i in range(len(students_list_sorted))}
print("Вариант решения 2:", list_averages2)
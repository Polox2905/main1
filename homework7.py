grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
g1=sum(grades[0]) / len(grades[0])
g2=sum(grades[1]) / len(grades[1])
g3=sum(grades[2]) / len(grades[2])
g4=sum(grades[3]) / len(grades[3])
g5=sum(grades[4]) / len(grades[4])
grades= [g1, g2, g3, g4, g5]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=sorted(students)
dictionary=dict(zip(students, grades))
print(dictionary)



def assign_grades(marks_list):
    grades = []
    for marks in marks_list:
        if marks >= 90:
            grades.append('A+')
        elif 80 <= marks < 90:
            grades.append('A')
        elif 70 <= marks < 80:
            grades.append('B')
        elif 60 <= marks < 70:
            grades.append('C')
        elif 50 <= marks < 60:
            grades.append('D')
        else:
            grades.append('F')
    return grades


marksList = [70, 99, 88, 50, 35]
print(assign_grades(marksList))

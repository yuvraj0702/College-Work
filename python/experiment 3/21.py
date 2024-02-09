try:
    
    marks_subject1 = float(input("Enter marks for Subject 1: "))
    marks_subject2 = float(input("Enter marks for Subject 2: "))
    marks_subject3 = float(input("Enter marks for Subject 3: "))
    marks_subject4 = float(input("Enter marks for Subject 4: "))
    marks_subject5 = float(input("Enter marks for Subject 5: "))
    

    total_marks = marks_subject1 + marks_subject2 + marks_subject3 + marks_subject4 + marks_subject5
    percentage = (total_marks / 500) * 100

    
    cgpa = percentage / 10

    
    if 0 <= cgpa <= 3.4:
        grade = 'F'
    elif 3.5 <= cgpa <= 5.0:
        grade = 'C+'
    elif 5.1 <= cgpa <= 6.0:
        grade = 'B'
    elif 6.1 <= cgpa <= 7.0:
        grade = 'B+'
    elif 7.1 <= cgpa <= 8.0:
        grade = 'A'
    elif 8.1 <= cgpa <= 9.0:
        grade = 'A+'
    elif 9.1 <= cgpa <= 10.0:
        grade = 'O (Outstanding)'
    else:
        grade = 'Invalid CGPA'

    
    print(f"\nPercentage: {percentage:.2f}%")
    print(f"CGPA: {cgpa:.2f}")
    print(f"Grade: {grade}")

except ValueError as e:
    print(f"Error: {e}")

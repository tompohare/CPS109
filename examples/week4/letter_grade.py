"""Assign a letter grade given a numeric grade.

A letter grade will be assigned in accordance with the
College’s Grading System:

A   93-100   C   73-76
A-  90-92    C-  70-72
B+  87-89    D+  67-69
B   83-86    D   63-66
B-  80-82    D-  60-62
C+  77-79    F   Below 60
"""

numeric_grade = int(input('Enter a numeric grade: '))

# chain comparison logic
# if start <= numeric_grade <= end:
#     assign letter grade

if numeric_grade >= 93:
    letter_grade = 'A'
elif 90 <= numeric_grade <= 92:
    letter_grade = 'A-'
elif 87 <= numeric_grade <= 89:
    letter_grade = 'B+'
elif 83 <= numeric_grade <= 86:
    letter_grade = 'B'
elif 80 <= numeric_grade <= 82:
    letter_grade = 'B-'
elif 77 <= numeric_grade <= 79:
    letter_grade = 'C+'
elif 73 <= numeric_grade <= 76:
    letter_grade = 'C'
elif 70 <= numeric_grade <= 72:
    letter_grade = 'C-'
elif 67 <= numeric_grade <= 69:
    letter_grade = 'D+'
elif 63 <= numeric_grade <= 66:
    letter_grade = 'D'
elif 60 <= numeric_grade <= 62:
    letter_grade = 'D-'
else:
    letter_grade = 'F'

print(f'Your letter grade for {numeric_grade} is {letter_grade}')
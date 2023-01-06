L = [25, 85, 87, 78, 77, 72, 81, 41, 43, 44, 47, 54, 58]

def round_grades(L):
    rounded_grades = []
    for grade in L:
        if grade < 40:
            rounded_grades.append(grade)
        else:
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                rounded_grades.append(next_multiple)
            else:
                rounded_grades.append(grade)
    return rounded_grades

round_grades(L)

print(round_grades(L))
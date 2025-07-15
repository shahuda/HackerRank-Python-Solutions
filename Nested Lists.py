if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    min_score = min(students, key=lambda x: x[1])[1]
    students = [student for student in students if student[1] != min_score]

    second_min = min(students, key=lambda x: x[1])[1]
    result = [student[0] for student in students if student[1] == second_min]
    result.sort()

    for name in result:
        print(name)

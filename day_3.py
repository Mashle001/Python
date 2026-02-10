n = int(input("enter a number of students marks: "))
m = [0] * n
section = 'j'

for i in range(n):
    m[i] = int(input("enter marks of student " + str(i+1) + ": "))

total_valid_students =0
total_fail_students =0

for i in range(n):
    if m[i] < 0 or m[i] > 100:
        print(m[i], "invalid")
    else:
        total_valid_students += 1

        if section == 'j':
            adjmarks = m[i] + 1
        elif section == 'k':
            adjmarks = m[i] - 1
        else:
            adjmarks = m[i]

        if adjmarks >= 90:
            print(m[i], "excellent")
        elif adjmarks >= 75:
            print(m[i], "very good")
        elif adjmarks >= 60:
            print(m[i], "good")
        elif adjmarks > 40:
            print(m[i], "average")
        else:
            total_fail_students += 1
            print(m[i], "fail")

print("total valid students:", total_valid_students)
print("total fail students:", total_fail_students)

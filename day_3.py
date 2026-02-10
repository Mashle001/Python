n = int(input("Enter a number of students marks: "))
m = [0]*n
section = 'j'
for i in range(n):
    m[i] = int(input("Enter marks of student " + str(i+1) + ": "))
    
total_valid_students = 0
total_fail_students = 0
for i in range(n):
        if m[i] < 0 or m[i] > 100:
            print("Invalid marks ")
        else: 
            total_valid_students += 1

            if section == 'j' :
                adjmarks = m[i] + 1
            elif section == 'k' :
                adjmarks = m[i] - 1
            else:
                adjmarks = m[i]


            if adjmarks >= 90:
                print("excellent")
            elif adjmarks >= 75:
                print("very good")
            elif adjmarks >= 60:
                print("good")
            elif adjmarks >= 40:
                print("average")
            else:
             total_fail_students += 1
             print("fail")




print("Total valid students: " + str(total_valid_students))
print("Total fail students: " + str(total_fail_students))
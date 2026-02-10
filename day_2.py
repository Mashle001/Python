# Taking inputs from user
studentid = input("enter student id: ")
email = input("enter email: ")
pwd = input("enter password: ")
ref = input("enter referral code: ")

is_valid = True



if len(studentid) != 7:
    is_valid = False
elif studentid[0] !='C':
    is_valid = False
elif studentid[1]!= 'S':
    is_valid = False
elif studentid[2] != 'E':
    is_valid = False
elif studentid[3]!= '-':
    is_valid = False
elif studentid[4] <'0' or studentid[4] > '9':
    is_valid = False
elif studentid[5]< '0' or studentid[5] > '9':
    is_valid = False
elif studentid[6] < '0' or studentid[6] > '9':
    is_valid = False




elif len(email) < 4:
    is_valid =False
elif '@' not in email:
    is_valid =False
elif '.' not in email:
    is_valid =False
elif email[0]== '@':
    is_valid= False
elif email[-1] == '@':
    is_valid =False
elif email[-4] != '.':
    is_valid = False
elif email[-3] != 'e':
    is_valid = False
elif email[-2] != 'd':
    is_valid =False
elif email[-1] != 'u':
    is_valid = False




elif len(pwd) < 8:
    is_valid =False
elif pwd[0] < 'A' or pwd[0] > 'Z':
    is_valid =False
elif not (
    ('0' <= pwd[0] <='9') or
    ('0' <= pwd[1] <='9') or
    ('0' <= pwd[2] <='9') or
    ('0' <= pwd[3] <='9') or
    ('0' <= pwd[4] <='9') or
    ('0' <= pwd[5] <='9') or
    ('0' <= pwd[6] <='9') or
    ('0' <= pwd[7] <='9')
):
    is_valid = False



elif len(ref) != 6:
    is_valid= False
elif ref[0] != 'R':
    is_valid =False
elif ref[1] != 'E':
    is_valid =False
elif ref[2] !='F':
    is_valid= False
elif ref[3] < '0' or ref[3] > '9':
    is_valid =False
elif ref[4] < '0' or ref[4] > '9':
    is_valid= False
elif ref[5] != '@':
    is_valid = False


if is_valid:
    print("approved")
else:
    print("rejected")

fullname = input("enter full name: ")
email = input("enter email ID: ")
mobile = input("enter mobile number: ")
age = int(input("enter age: "))

valid = True

if fullname.startswith(" ") or fullname.endswith(" "):
    valid = False
elif fullname.count(" ") < 1:
    valid = False

if '@' not in email or '.' not in email or email[0] == '@':
    valid = False

if len(mobile) != 10 or not mobile.isdigit() or mobile[0] == '0':
    valid = False

if age < 18 or age > 60:
    valid = False


if valid:
    print("user profile is VALID")
else:
    print("user profile is INVALID")

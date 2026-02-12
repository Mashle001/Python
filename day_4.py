# data = ['hari',645,'vishnu',648,"yesh",646]
data = [99,"hii","","hello","brao",100,101]
num = []
string = []

count_num = 0
count_string = 0

for i in data:
    if i == "":
        continue
    if type(i) == int:
        num.append(i)
        count_num = count_num + 1
    elif type(i) == str:
        string.append(i)
        count_string = count_string + 1


name = 'hari krishna'
length = len(name)
if length % 2 == 0:
    if len(num) > 0:
        num.pop(0)
    if len(string ) > 0:
        string.pop(0)
else:
    if len(num) > 0:
        num.pop()
    if len(string ) > 0:
        string.pop()

print("numbers list:" , num)
print("string list: ",string)
print("total numbers: ",count_num)
print("total strings: ",count_string)


    


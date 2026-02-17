# weights = [1, 3, 5, 7, 9, -11, 13, 15, 17, 19]
weights= [4, 18, 70, -2, 30, 55, 0]

full_name = "hari"
without_space = ""
for i in full_name:
    if i == " ":
        continue
    without_space = without_space + i

L =0
for ch in without_space:
    L= L+1
pli= L%3

very_light =[]
normal_load =[]
heavy_load =[]
overload =[]
invalid_entries =[]


for wt in weights:
    if wt <0:
        invalid_entries.append(wt)

    elif wt<=5:
        very_light.append(wt)


    elif wt <=25:
        normal_load.append(wt)

    elif wt <=60:
        heavy_load.append(wt)

    else:
        overload.append(wt)


total_valid = 0

for i in very_light:
    total_valid = total_valid +1


for i in normal_load:
    total_valid = total_valid+ 1

for i in heavy_load: 
    total_valid = total_valid+ 1

for i  in overload:
    total_valid = total_valid +1


affected_count = 0
if pli == 0:
    for item in overload:
        invalid_entries.append(item)
        affected_count = affected_count + 1
    
    overload = []
    applied_rule = "rule A"

elif pli == 1:
    for item in very_light:
        affected_count = affected_count + 1
    
    very_light = []
    applied_rule = "rule B"

else:

    for item in very_light:
        affected_count = affected_count + 1
    for item in overload:
        affected_count = affected_count + 1
    very_light = []
    overload = []
    applied_rule = "rule C"

print("full name length (L):", L)
print("Pli value:", pli)
print("applied Rule:", applied_rule)
print("total  valid Weights:", total_valid)
print("affected items due to pli:", affected_count)

print("final loading Plan:")
print("very_light:", very_light)
print("normal_load:", normal_load)
print("heavy_load:", heavy_load)
print("Overload:", overload)
print("invalid entries:", invalid_entries)
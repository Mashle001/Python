
# energy_readings = [45, 120, 200, 30, 75, 160, -10, 55, 20, 180]
# energy_readings = [25, 40, 60, 70, 80, 45]
# energy_readings = [-5, -20, 30, 140, 160, 170]
energy_readings = [10, 15, 20, 25]

categories = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

for e in energy_readings:
    if e < 0:
        categories["invalid"].append(e)
    elif e <= 50:
        categories["efficient"].append(e)
    elif e <= 150:
        categories["moderate"].append(e)
    else:
        categories["high"].append(e)


validreadings = [e for e in energy_readings if e >= 0]
total_consumption = sum(validreadings)


summary =(total_consumption,len(energy_readings))

high_count =len(categories["high"])
efficient_count = len(categories["efficient"])
moderate_count =len(categories["moderate"])

overconsumption = high_count > 3
balanced_usage =abs(efficient_count - moderate_count)<= 1
energy_waste = total_consumption >600



if energy_waste:
    result = "energy waste detected"
elif balanced_usage:
    result = "efficient campus"
elif overconsumption:
    result ="Moderate usage"
else:
    result ="Moderate usage"


print("Categorized Readings:",categories)
print("Total Consumption:",summary[0])
print("Number of Buildings:",summary[1])
print("Efficiency Result:",result)
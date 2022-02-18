import json
import pandas as pd
import matplotlib.pyplot as plot

crime_json = open('C:\\Users\\Lauren\\source\\repos\\Homework\\FBI_CrimeData_2016.json', 'r')
crime_list = json.load(crime_json)
crime_json.close()

violent_by_region = {}
nonviolent_by_region = {}
murder_by_region = {}
    
murder = ['Murder']
violent_crimes = ['Rape', 'Robbery', 'Assault', 'Murder']
nonviolent_crimes = ['Burglary', 'Theft', 'Vehicle_Theft']

def accum_crime (area, crimes, murder_list):
    for record in murder_list:
        for key, value in record.items():
            for crime in crimes:
                if crime == key:
                    if record[area] in murder_by_region:
                        murder_by_region.update({record[area]:int(murder_by_region[record[area]]) + int(value)})
                    else:
                        murder_by_region.update({record[area]:int(value)})
        return murder_by_region

def accum_values (value_dict):
    for key, value in value_dict.items():
        result = 0
        result += value
        value_dict[key] = result
    return value_dict

def bar_chart (dictionary):
    regions = ['South', 'West', 'Northeast', 'Midwest']
    printed_dict ={'Region' :pd.Series(list(dictionary.keys())), 'Crime':pd.Series(list(dictionary.values()))}
    printed = pd.DataFrame(printed_dict)
    printed.plot.bar(x= 'Region', y= 'Crime', legend= False, color= ['red', 'blue', 'green', 'purple'])

murder_by_region = accum_crime('Region', murder, crime_list)
violent_by_region =  accum_crime ('Region', violent_crimes, crime_list)
nonviolent_by_region = accum_crime ('Region', nonviolent_crimes, crime_list)

states_murder = accum_crime('State', murder, crime_list)
states_violent = accum_crime('State', violent_crimes, crime_list)

states = dict([(k,[states_murder[k], states_violent[k]]) for k in states_murder])
states = accum_values(states_violent)    

print(murder_by_region)
print(violent_by_region)
print(nonviolent_by_region)

print(f"\n{states}\n")

sum = 0
for items in states.values():
    sum += items

average = int(sum/len(states.values()))

print(f"\nNational Average Violent Crime: {average}\n")
print(f"\n State Crimes Distance from Mean")

for key, value in states.items():
    print (f"{key:21} {value:>10} {value - average:>10}")


print("\nMurder by Region, Number of Incidents")
for key, value in murder_by_region.items():
    print(f"{value} - {key}\n")
bar_chart(murder_by_region)

print("Violent Crimes by Region, Number of Incidents")
for key, value in violent_by_region.items():
    print (f"{value} - {key}\n")
bar_chart(violent_by_region)


print("Non-violent Crimes by Region, Number of Incidents")
for key, value in nonviolent_by_region.items():
    print(f"{value} - {key}")
bar_chart(nonviolent_by_region)
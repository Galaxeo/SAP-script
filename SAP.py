from datetime import datetime
from operator import itemgetter
import csv
f = open(r"C:\Users\Justin\Downloads\UE Locations for AT&T and pCell Testing at SAP  - June 29, 2021.csv", "r")
csv_f = csv.reader(f)
datalist = list(csv_f)
lst = []
returnlst = []
number1 = 0
phoneorip = input("Input either '#' or 'IP' for phone # input or IP input respectively: ")
if phoneorip == "#":
    numinput = input("Please put in the phone #s in a comma separated list: ")
    lst = numinput.split(", ")
    lst = sorted(lst)
elif phoneorip.lower() == "ip":
    start = datetime.now()
    print("Copypaste the 172. IPs and enter 'done' when done: ")
    while True:
        inp = input()
        if len(inp) == 11:
            lst.append(inp[7] + "0" + inp[9:])
        elif len(inp) == 10:
            lst.append(inp[7] + "00" + inp[9])
        elif len(inp) == 12:
            if inp[7] == "0":
                lst.append(inp[9:])
            else:
                lst.append(inp[7] + inp[9:])
        elif inp.lower() == "done":
            break
    for item in lst:
        print(item)
    lst = sorted(lst)
else:
    raise ValueError("Please enter only # or IP")
counter = 0
for item in lst:
    counter+=1
for row in datalist:
    if row[3] == None:
        continue
    for num in lst:
        if row[3] == num:
            returnlst.append([num, "Sect. ", row[5], "Row ", row[7], "Pos. ", row[8]])
        else:
            continue
number = 0
print(number1)
returnlst = sorted(returnlst, key=itemgetter(2))
for item in returnlst:
    print(item[0], item[1] + item[2], item[3] + item[4], item[5] + item[6])
    number+=1
if counter == number:
    print("Good to go")
print(datetime.now() - start)
#Additional code if people want to do collect by row, section, or sort the list by number
# sortask = input("row, section, or #(number) ")
# if sortask.lower() == "section":
#     #Below is categorized by section
#     returnlst = sorted(returnlst, key=itemgetter(2))
#     for item in returnlst:
#         print(item[0], item[1] + item[2], item[3] + item[4], item[5] + item[6])
#         number+=1
# elif sortask.lower() == "row":
#     #Below is categorized by row
#     returnlst = sorted(returnlst, key=itemgetter(4))
#     for item in returnlst:
#         print(item[0], item[1] + item[2], item[3] + item[4], item[5] + item[6])
# elif sortask.lower() == "#" or sortask.lower() == "number":
#     returnlst = sorted(returnlst, key=itemgetter(0))
#     for item in returnlst:
#         print(item[0], item[1] + item[2], item[3] + item[4], item[5] + item[6])
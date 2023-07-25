etoDict = {"fName": "Eto", "lName": "Banas",
           "address": "123 Main St"}

print("May Name: ", etoDict["fName"])

etoDict["address"] = "215 North St"

etoDict['city'] = "Pittsburgh"

print("Is there a city: ", "city" in etoDict)

print(etoDict.values())

print(etoDict.keys())

for k, v in etoDict.items():
    print(k, v)


# if key is available, else print "Not here"

print(etoDict.get("mName", "Not Here"))

del etoDict["fName"]

for i in etoDict:
    print(i)

etoDict.clear()

employees = []

fName, lName = input("Enter Employee Name: ").split()

employees.append({'fName': fName, 'lName': lName})
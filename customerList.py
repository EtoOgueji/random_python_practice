customers = []

while True:
    createEntry =  input("Enter Customer (Yes/No): ")
    createEntry = createEntry.lower()

    if createEntry == "no":
        break
    else:
        fName, lName = input("Enter Customer Name: ").split()

        customers.append({'fName': fName, 'lName': lName})

for cust in customers:
    print(cust['fName'], cust['lName'])
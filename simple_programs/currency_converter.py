with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}

for line in lines:
    parsed = line.split("\t")
    # print(parsed)
    currencyDict[parsed[0]] = float(parsed[1])

amount = int(input("Enter amount in INR you want to convert: "))
currencyName = input("Enter name of currency you want to convert this amount to: ")

converted_currency = round(amount * currencyDict[currencyName] , 2)
print(f"{amount} INR is equal to {converted_currency} {currencyName}")

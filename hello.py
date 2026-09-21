#  Input we need from the user
# Total rent.
# Total food ordered for snaking
# Electricity units spend
# Charge per unit
# persons living in Room/Flat


#   Output
# Total amount you've to pay is

rent = int(input("Enter your Hostel/Flat rent = "))
food = int(input("Enter your amount of food  ordered = "))
electricitySpend = int(input("Enter the total of electricity Spend = "))
ChargePerUnit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of person living in room/flat = "))


totalBill = electricitySpend * ChargePerUnit

output = (food + rent + totalBill) // persons

print("Each person will pay = ", output)
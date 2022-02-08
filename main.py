### User Input ###
# Starting Amount DONE
# Income Amount and Payday DONE
# Bill Amount and Due Dates 
# Date to Simulate to

userInput_startAmount = input("Current Amount(xx.xx): $")
userInput_Income = input("Income (xx.xx): $")
userInput_PayDayRate = input("Payday Every X Days: ")
userInput_numberBills = input("How Many Bills Do You Have?: ")

#Bill Amount and DueDates
billList = []
count = 0

while count < int(userInput_numberBills):
    billFormatDict = {}
    billFormatDict['Bill'] = input('Bill Name: ')
    billFormatDict['Amount'] = input('Amount: ')
    billFormatDict['Due Date'] = input('Due Date: ')

    billList.append(billFormatDict)
    billFormatDict = {}

    count += 1

print(billList)


### OUTLINE of Project ###

# Track Starting Income && Paydays

# Track Bills & Due Dates

# Progress Time
#     If day is equal to the day of Payday OR Bill Due, add OR deduct X amount.


### Program Output ###
# Amount in "Account" After Simulation
### User Input ###
# Starting Amount DONE
# Income Amount and Payday DONE
# Bill Amount and Due Dates 
# Date to Simulate to

userInput_startAmount = input("Current Amount(xx.xx): $")
userInput_Income = input("Income (xx.xx): $")
userInput_PayDayRate = input("Payday Every X Days: ")

# Whats the BEST data collection type for storing bills?

### SAMPLE DATA ###
# due date(date) : amount(float)
# 1 : 700
# 10 : 125
# 14 : 14.99
# 30 : 20

tag = True
billsAmounts = []

while tag == True:
    dict = {}
    key = input("name of bill: ")
    if key == "done":
        tag = False

    value = input("amount: ")
    if value == "done":
        tag = False
    dict.update({str(key):int(value)})

    print("\n")
    billsAmounts.append(dict)
    print(billsAmounts)
    


### OUTLINE of Project ###

# Track Starting Income && Paydays

# Track Bills & Due Dates

# Progress Time
#     If day is equal to the day of Payday OR Bill Due, add OR deduct X amount.


### Program Output ###
# Amount in "Account" After Simulation
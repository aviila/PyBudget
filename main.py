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
count = 1

while count < int(userInput_numberBills) + 1:
    print("Bill {} / {}".format(count,userInput_numberBills))

    billFormatDict = {}
    billFormatDict['Bill'] = input('Bill Name: ')
    billFormatDict['Amount'] = input('Amount: ')
    billFormatDict['Due Date'] = input('Due Date: ')

    billList.append(billFormatDict)
    billFormatDict = {}

    count += 1

print(billList)

### How Date Simulation is going to work ###
from datetime import date, datetime, timedelta

#For Computer Use
compTodayDay = date.today()

#For Human Use (comp -> human)
humanTodayDay = compTodayDay.strftime("%B %d, %Y")

print(compTodayDay.day)
print(humanTodayDay)
print("\n")

#For Human Use
userDate = "February 10 2022"
trackingDay = "Mar 15 2022"
#For Computer Use (human -> comp)
compUserDate = datetime.strptime(userDate, '%B %d %Y').date()
compTrackingDay = datetime.strptime(trackingDay, '%b %d %Y').date()

# if compTrackingDay > compUserDate:


print(compUserDate)
print(compTrackingDay)
print("\n")

### Bake Bill / Payday in While Loop ###
while compUserDate <= compTrackingDay:
    print(compUserDate.strftime("%B %d, %Y"))
    compUserDate = compUserDate + timedelta(days=1)


### OUTLINE of Project ###

# Track Starting Income && Paydays

# Track Bills & Due Dates

# Progress Time
#     If day is equal to the day of Payday OR Bill Due, add OR deduct X amount.


### Program Output ###
# Amount in "Account" After Simulation
from datetime import date,datetime, timedelta

class Bills:
    def __init__(self,billName,billDate,billPrice):
        self.billName = billName
        self.billDate = billDate
        self.billPrice = billPrice
    

def askBills(start=True):
    billList = []
    userInput_startBalance = float(input("Starting Balance: $"))
    userInput_PaydayRate = int(input("How many days between paydays?: "))
    userInput_UserPay = int(input("How much do you get paid?: "))

    while start == True:
        userInput_billName = input("Bill Name: ")
        userInput_billDate = datetime.strptime(input("Bill Due Date: (Day) "),"%d").day
        userInput_billPrice = float(input("Bill Price: $"))
        
        billList.append(Bills(userInput_billName,userInput_billDate,userInput_billPrice))

        doneInput = input("Done? y/n: ")
        
        if doneInput == "y":
            return billList, userInput_startBalance, userInput_PaydayRate, userInput_UserPay

def simulate(billList, userBalance, userPayRate, userPay):
    startDate = datetime.today()
    daysPassed = 0
    finalDate = datetime(2022,5 , 20)

    while startDate <= finalDate:
        print("{}".format(startDate.date()))
        
        # if daysPassed % PayRate == 0:
        # userBalance =+ userIncome

        for bill in billList:

            if startDate.day == bill.billDate:
                print("{}".format(startDate.date()))
                print("{} is Due {} for the Amount of ${}".format(bill.billName, startDate.date(), bill.billPrice))
                userBalance -= bill.billPrice
                print("New Balance: {}".format(userBalance))
        
        startDate += timedelta(1)
        daysPassed += 1

        if daysPassed % userPayRate == 0:
            userBalance += userPay
            print("Payday! + {} Balance: {}".format(userPay, userBalance))

def main():
    billList, userBalance, userPayRate, userPay =  askBills()

    simulate(billList, userBalance, userPayRate, userPay)

if __name__ == "__main__":
    main()
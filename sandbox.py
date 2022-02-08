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

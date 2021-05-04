# today's date
from MonthDictionary import month_def
from datetime import date
today = date.today()
today_date = today.strftime("%m/%d/%Y")


# finds the client's DOB
date_of_birth = input("Enter your Date of Birth __/__/____: ")
dates = date_of_birth.split('/')
month = dates[0]
day = int(dates[1])
year = int(dates[2])

tdates = today_date.split('/')
tmonth = tdates[0]
tday = int(tdates[1])
tyear = int(tdates[2])

tt_days = 0
for tdate in tdates:
    tt_days = month_def.get(tmonth) + day
tdecimal_days = tt_days/365

total_days = 0
for date in dates:
    total_days = month_def.get(month) + day
decimal_days = total_days/365

age = (tyear + tdecimal_days) - (year + decimal_days)
print(f"your age is {age}")

# calculate when the first RMD will be
new_first_rmd = 73 + year
old_first_rmd = 71 + year

if year > 1949:
    print(f"Your first RMD is due by April 1st, {new_first_rmd}")
elif year == 1949 and int(month) >= 7:
    print(f"Your first RMD is due by April 1st, {new_first_rmd}")
elif year == 1949 and int(month) < 7:
    print(f"Your first RMD was due by April 1st, {old_first_rmd}")
elif year < 1949 and int(month) < 7:
    print(f"Your first RMD was due by April 1st, {old_first_rmd}")
else:
    print(f"Your first RMD was due by April 1st, {72 + year}")

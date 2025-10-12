months = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

s = input().strip()
splits = s.split()

month = splits[0]
day = int(splits[1][:-1])
year = int(splits[2])
hour, minute = map(int, splits[3].split(':'))

def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

if is_leap(year):
    month_days[1] = 29

days_passed = sum(month_days[:months[month]-1]) + (day - 1)
current_minutes = days_passed * 24 * 60 + hour * 60 + minute
total_minutes = sum(month_days) * 24 * 60

print(current_minutes / total_minutes * 100)



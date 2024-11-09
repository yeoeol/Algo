DAYS = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
one = {1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 4:30, 6:30, 9:30, 11:30, 2:28}

x, y = map(int, input().split())
total = 0
for i in range(1, x):
    total += one[i]

ind = (total+y)%len(DAYS)
print(DAYS[ind])
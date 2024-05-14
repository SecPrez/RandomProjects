from datetime import datetime, timedelta

d = datetime(1901, 1, 1)

final_dt = datetime(2000, 12, 31)
sunday_count = 0
while d < final_dt:

    if d.weekday() == 6 and d.day == 1:
        sunday_count += 1
    d = d + timedelta(days=1)
print(sunday_count)

day_before_leap_year = datetime(2000, 2, 28)
print(day_before_leap_year.day)
day_before_leap_year += timedelta(days=1)
print(day_before_leap_year.day)
day_before_leap_year += timedelta(days=1)
print(day_before_leap_year.day)

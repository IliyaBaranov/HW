import datetime
def search_timestamp(timeset):
    timeset = datetime.datetime.fromtimestamp(timeset)
    timeset_delta = datetime.timedelta(weeks=2)
    return datetime.datetime.timestamp(timeset - timeset_delta)


sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'
some_day = 1014163200
# 1
s1_dt = datetime.datetime(2014, 1, 1, 2, 43)
s2_dt = datetime.datetime.strptime(sample2, '%H:%M %d/%m/%y')
s3_dt = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
s4_dt = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print('#1')
print(s1_dt)
print(s2_dt)
print(s3_dt)
print(s4_dt)
print('#2')
# 2
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(today)
print(yesterday)
print(tomorrow)
print('#3')
# 3
some_day_2 = datetime.datetime.fromtimestamp(some_day)
print(some_day_2.__format__('%d.%m.%Y'))
print('#4')
# 4
timeset = float(input('Please enter timestamp: '))
print(search_timestamp(timeset))

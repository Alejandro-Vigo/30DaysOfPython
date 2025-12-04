#Day 16: 30 Days of python programming

#import datetime
#print(dir(datetime)) #To know the available functions

from datetime import datetime
now= datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp())

print(now.strftime("%m/%d/%Y, %H:%M:%S"))

date = '5 December, 2019'
print((datetime.strptime(date, "%d %B, %Y")))

from datetime import date
new_year = date(2026, 1, 1)
now_date = date.today()
print(new_year-now_date)

unix_time = date(1970,1,1)
print(now_date-unix_time)

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {event}")
log_event("User logged in")

from datetime import timedelta
def schedule_post(title, days_from_now):
    publish_date = datetime.now() + timedelta(days=days_from_now)
    print(f"Post '{title}' will be published on {publish_date.strftime('%Y-%m-%d %H:%M:%S')}")
schedule_post("My New Post", 31) 
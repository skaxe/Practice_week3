from datetime import datetime, date, timedelta
dt_now = datetime.now()

delta_1 = timedelta(days = 1)
yesterday = dt_now-delta_1
#print(yesterday)
print_yesterday = yesterday.strftime ('%d. %m. %Y')
print(print_yesterday)
print_now = dt_now.strftime ('%d. %m. %Y')
print(print_now)
delta_30 = timedelta(days = 30)

mounth_ago = dt_now - delta_30
print_mounth = mounth_ago.strftime ('%d. %m. %Y')
print(print_mounth)
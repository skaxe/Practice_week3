from datetime import datetime, date, timedelta
date_str = '01/03/1995'
#первартиь строку в обьект datetime
date_dt = datetime.strptime(date_str, '%m/%d/%Y')
date_dt
print(date_dt)

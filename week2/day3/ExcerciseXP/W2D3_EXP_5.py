#  Exercise 5: Amount of time left until January 1st

import datetime as dt

def show_current_date_time():
    now = dt.datetime.now()
    return now

now = show_current_date_time()

next_year = now.year + 1
new_year = dt.datetime(next_year, 1, 1)

time_difference = new_year - now

print(f"Time left until January 1st: {time_difference}")
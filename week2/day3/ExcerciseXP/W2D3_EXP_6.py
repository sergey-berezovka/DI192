# Exercise 6: Birthday and minutes
import datetime as dt

def minutes_lived(birthdate_str):
    birthdate = dt.datetime.strptime(birthdate_str, "%Y-%m-%d")

    now = dt.datetime.now()
    
    time_difference = now - birthdate
    
    minutes = int(time_difference.total_seconds() / 60)
    
    print(f"You have lived {minutes:,} minutes.")

minutes_lived ("1979-01-01")
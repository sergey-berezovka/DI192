def difference (a,b):
    return a - b
print(difference(2,2))
print(difference(0,2))

def print_day (num):
   days = [
      "Sunday", "Monday", "Tuesday", "Wednеsday", "Thirsday", "Friday", "Saturday"
      ]
   if 1 <= num <= 7:
    return days [num - 1]
   return None
print(print_day(4))
print(print_day(0))


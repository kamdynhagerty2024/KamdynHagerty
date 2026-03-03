#Name: Section5.14problem1
#Purpose: Conditionals
#Author: KamdynHagerty
#Created: 3/2/26



def get_day_name(day_number):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    if 0 <= day_number <= 6:
        return days[day_number]
    else:
        return "Invalid day number"


print(get_day_name(0))
print(get_day_name(1))
print(get_day_name(2))
print(get_day_name(3))
print(get_day_name(4))
print(get_day_name(5))
print(get_day_name(6))

#Name: Section6.9problem7
#Purpose: FruitfulFunctions
#Author: KamdynHagerty
#Created: 3/9/26


def to_secs(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds
print(to_secs(2, 30, 10))  
print(to_secs(2, 0, 0))    
print(to_secs(0, 2, 0))    
print(to_secs(0, 0, 42))   

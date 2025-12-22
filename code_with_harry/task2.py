
import time 
name = input("Enter your name:")
timestamp = time.strftime('%H:%M:%S%p')
print(timestamp)
timestamp = int(time.strftime('%H'))

recent_time=timestamp
# recent_time=int(input("enter hour:"))
if 0 <=  recent_time and  recent_time <12:
    print(f"good morning {name}")
    

elif 12<=  recent_time and  recent_time<17:
    print(f"good afternoon {name}")

elif 17<=  recent_time and  recent_time< 19:
    print(f"good evening {name}")    
else:
    print(f"good night {name}")     



















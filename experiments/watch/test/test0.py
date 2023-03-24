"""
display the time and date
"""

import datetime
import time
print(time.strftime("%H:%M:%S"))


e = datetime.datetime.now()

print("Current date and time = %s" % e)
print("Today's date:&nbsp; = %s/%s/%s" % (e.day, e.month, e.year))
print("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))


print("Printed immediately.")



time.sleep(5)
print("Printed after 5 seconds.")

e2 = datetime.datetime.now()

print("The time after 5 seconds: = %s:%s:%s" % (e.hour, e.minute, e.second))


#get the diff in the time 
diff = abs(e2-e)

print(diff)
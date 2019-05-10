import time
import datetime

print(time.time())
print(time.localtime())
print(time.gmtime())

print(time.strftime("%a %Y-%m-%d %H:%M:%S", time.gmtime()))

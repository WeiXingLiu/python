import time
import calendar

tTime = time.time()
localTime = time.localtime(time.time())
myTime = time.asctime(localTime)
print(tTime, localTime, myTime)

def test() :
    print('my')

test()

month = calendar.month(2018, 9)
# day = calendar.day
print(month)


age = 18
print('123%s' % (age))

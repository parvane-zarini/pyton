onehaver = 10
tm = input('Enter time:')
try: 
    time = int(tm)
except: 
    time = -1
if time <= 40:
    pay = time * onehaver
    print(pay)
elif time > 40:
    ezaf= time - 40
    pay= 40 * onehaver + ezaf * 15
    print(pay)
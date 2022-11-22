hours = 35.0 
rate = 12.50 
pay = hours * rate 
print(pay)

x = 2
x = x + 2
print(x)

x = 3.9 *  x  * ( 1  -  x )
print(x)

xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)

x = 1 + 2 ** 3 / 4 * 5
print(x)

ddd = 1 + 4
print(ddd)

eee = 'hello ' + 'there'
print(eee)

print(float(99) + 100)
i = 42
type(i)
f = float(i)
print(f)
type(f)

print(10 / 2) 
print(9 / 2) 
print(99 / 100) 
print(10.0 / 2.0) 
print(99.0 / 100.0) 


nam = input('Who are you? ')
print('Welcome', nam)

inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')



x = 5
if x == 5 : 
    print('Equals 5')
if x > 4 : 
   print('Greater than 4')
if  x >= 5 :
    print('Greater than or Equals 5')
if x < 6 : print('Less than 6') 
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')


x = 5
if x > 2 :
     print('Bigger than 2')
     print('Still bigger')
print('Done with 2')

for i in range(5) :
     print(i)
     if i > 2 : 
         print('Bigger than 2')
     print('Done with i', i)
print('All Done') 



x = 42
if x > 1 :
    print('More than one')
    if x < 100 : 
        print('Less than 100') 
print('All done')


x = 4

if x > 2 :
    print('Bigger')
else :
    print('Smaller')

print('All done')



if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')



x = 0 
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')


x = 5 
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')




x = 20
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')



# No Else
x = 5
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')

print('All done')



if x < 2 :
    print('Below 2')
elif x >= 2 : 
    print('Two or more')
else :
    print('Something else')



astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)






astr = 'Bob'
try:
    print('Hello') 
    istr = int(astr)
    print('There') 
except:
    istr = -1

print('Done', istr) 



rawstr = input('Enter a number:')
try: 
    ival = int(rawstr)
except: 
    ival = -1

if ival > 0 :  
    print('Nice work')
else:  
    print('Not a number')



def thing():
    print('Hello')
    print('Fun')
 
thing()
print('Zip')
thing()



big = max('Hello world')
print(big)

tiny = min('Hello world')
print(tiny)





print(float(99) / 100)
i = 42
type(i)
f = float(i)
print(f)
type(f)
print(1 + 2 * float(3) / 4-5)
 

x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
x = x + 2
print(x)



x = 5
print('Hello')

def print_lyrics(): 
   print("I'm a lumberjack, and I'm okay.")
   print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)

def greet(lang):
     if lang == 'es':
        print('Hola')
     elif lang == 'fr':
        print('Bonjour')
     else:
        print('Hello')
 
greet('en')
greet('es')
greet('fr') 


def greet1():
    return "Hello"

print(greet(), "Glenn")
print(greet(), "Sally")


def greet2(lang):
     if lang == 'es':
         return 'Hola'
     elif lang == 'fr':
         return 'Bonjour'
     else:
         return 'Hello'
 
print(greet('en'),'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')
 
big = max('Hello world')
print(big)


def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)





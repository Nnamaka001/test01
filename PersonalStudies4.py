'''import mymodule
a = mymodule.person1['age']
print(a)'''

'''import platform
x = platform.system()
print(x)'''

'''import platform
x = dir(platform)
print(x)'''

'''from mymodule import person1
print(person1)
print(person1['age'])'''

'''import datetime
print(dir(datetime))
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.time())
print(x.strftime('%A'))
print(x.date())

y = datetime.datetime(2022, 12, 25)
print(y)
print(y.strftime('%b'))'''

'''x = abs(-7.25)
print(x)'''

'''x = pow(4,3)
print(x)'''

'''import math as m
x = m.pow(3,3)
print(x)'''

'''import json
x = '{"name" : "John", "age" : 30, "city" : "Newyork"}'
y = json.loads(x)
print(y['age'])'''

'''import re
txt = 'The rain in Spain'
x = re.search("^The.*Spain$", txt)
print(x)'''

'''import re
txt = 'The rain in Spain'
x = re.findall("ai", txt)
print(x)'''

'''import re
txt = 'The rain in Spain'
x = re.search("\s", txt)
print('The first white-space character is located in position: ', x.start())'''

'''import re
txt = 'The rain in Spain'
x = re.split("\s", txt)
print(x)'''

'''import re
txt = 'The rain in Spain'
x = re.sub("\s", "9", txt)
print(x)'''

'''try:
    print(x)
except:
    print('An exception has occured')'''

'''try:
    print(x)
except NameError:
    print('Variable x is NOT defined')
except:
    print('Something else is wrong')'''

'''try:
    print('Hello')
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')'''

'''try:
    print(x)
except:
    print('Something went wrong')
finally:
    print("The 'try except' is finished")'''

'''try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong while writing to file")
    finally:
        f.close()
except:
    print("Somethine went wrong while opening file")'''

'''x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")'''

'''x = "Hello"
if not type(x) is int:
    raise TypeError("Only integars are allowed")'''

'''price = 49
txt = 'The price is {} dollars.'
print(txt.format(price))'''

'''quantity = 3
itemno = 567
price = 49
myorder = 'I want {} pieces of item number {} for {:.2f} dollars.'
print(myorder.format(quantity, itemno, price))'''

'''quantity = 3
itemno = 567
price = 49
myorder = 'I want {0} pieces of item number {1} for {2:.2f} dollars.'
print(myorder.format(quantity, itemno, price))'''

'''age = 36
name = 'Zubby'
txt = 'His name is {1}. {1} is {0} years old.'
print(txt.format(age, name))'''

'''myorder = 'I have a {carname}. It is a {model}.'
print(myorder.format(carname = 'Ford', model = 'Mustang'))'''

'''f = open('demofile.txt', 'r')
print(f.read())'''

'''f = open('C:\\Users\methy\demofile.txt', 'r')
print(f.read())'''

'''f = open('demofile.txt', 'r')
for x in f:
    print(x)'''

'''f = open('demofile2.txt', 'a')
f.write('Now the file has more content!')
f.close()'''

'''f = open('demofile2.txt', 'r')
print(f.read())'''

'''f = open('demofile3.txt', 'w')
f.write('Woops! I have deleted the content')
f.close()

f = open('demofile3.txt', 'r')
print(f.read())'''

#f = open("myfile.txt", "x")

'''import os
#os.remove('myfile.txt')

if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('The file does not exist')'''

import os
os.rmdir('myfolder')

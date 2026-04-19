#print output
print("Hello, World!")

#indentation
if 5>2:
    print('learning indentation')

#type casting
a=int(3)
b=float(3)
c=str(3)
print(a,type(a),b,type(b),c,type(c))

#many values to multiple variables
x,y,z=12,14,16
print(x,y,z)

#unpack a collection
fruits=['apple','banana','mango']
m,n,o=fruits
print(m,n,o)

#global variable
d='pyhton is awesome'
def myfunc():
     print('i am saying' ,d)
myfunc() 

#create a variable inside function same as global variable 
e='elephant'
def myfunc2():
    e='elegant'
    print(e)
myfunc2()    
print(e)    

#create random number 
import random
print(random.randrange(1,10))

#looping through a string 
for x in 'banana':
    print(x)

#check string 
text='bangladesh in a beautiful country'
print('bangladesh' in text)
print('tiger' not in text)
if 'country' in text:
    print('yes country is in the text')
    
#function string 
age2=25
text2=f'my name is sayem . i am {age2} years old'
print(text2)  

#comment added fot git test 

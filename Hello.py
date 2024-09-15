'''
x = 0
while x<5:
 	print(x)
 	x = x + 2




n = int(input('Enter the number of terms - '))
x = 0
for i in range (0,n):
    j = 2*i + 1 
    x = x + j
print(x)


print('1. Area of Rectangle:')
print('2. Area of Square:')
print('3. Area of circle:')
c = int(input('enter choice'))

if c==1:
	l = int(input('enter the lenght'))
	b = int(input('enter the breadth'))
	
	a = l*b
	print ('the area is:', a)

elif c==2:
	l = int(input('enter length:'))
	a = l*l
	print('the area is:', a)
else:
	print('enter a valid input')




a = input("enter a numbers:")
b = input("enter a numbers:")
c = input("enter a numbers:")
if a>b and a>c:
    print("a")
elif b>c and b>a:
    print("b")
else:
    print("c")





a=int(input('Enter number1:'))
b=int(input('Enter number2:'))
c=int(input('Enter number3:'))
import sys
if a>b and a>c:
    mx=a
elif b>a and b>c:
    mx=b
elif c>a and c>b:
    mx=c
elif a==b and b==c and c==a:
    print('All are same.')
    sys.exit()
elif a==b or b==c or c==a:
    print('Two are same.')
    sys.exit()
print('Maximum is',mx)



x = 1
y = 1
s = 0
n = int(input('enter no. of terms:'))
print(x, y, end = ' ')


i = 0
while i<=n-3:
	s = x+y
	print(s, end = " ")
	y = x
	x = s
	i = i+1

	
	
num1 = int(input("Enter a number: "))
 
if num1 > 1:
   for i in range(2,num1):
       if (num1 % i) == 0:
           print(num1,"is not a prime number")
           print(i,"times",num1//i,"is",num1)
           break
   else:
       print(num1,"is a prime number")
        
else:
   print(num1,"is not a prime number")	

	
	
for i in range(2,13)
if n%i == 0:
	print('not prime')
else:
	print('prime')


flag = 0
n=int(input("enter : "))
for i in range(2,n):
    if(n%i==0):
        flag = 1
       
       
if flag == 0:
	print('prime')
else:
	print('not prime')



n = int(input('enter a no.:'))
s = 0
while(n>0):
    r = n%10
    n = int(n/10)
    s+=int(r)
    
print(s)  




f = 123
s = 0
while f>0:
	a = f%10
	s = s+a
	f = int(f/10)
print(s)


'''

for i in range(3):
	for j in range(3):
		print('1',end = ' ')
	print( )




for i in range(3):
	for j in range(3):
		print(i+1,' ', end = ' ')
	print()



for i in range(3):
	for j in range(3):
		print(3-i, end = ' ')
	print()




for i in range(3):
	for j in range(i+1):
		print('1 ',end = '' )
	print()


'''

num=int(input("Enter the number of rows to print: "))
for q in range(1,num+1):
    for x in range(q):
        print(q, end=" ")
    print("")


'''

for i in range(3):
	for j in range(i+1):
		print(3-i,' ', end ='')
	print()


'''

n = int(input())
 
for i in range(n):
    for j in range(i):
        print(end = " ")
    print(i+1)




n=int(input('Enter'))
for i in range(n):
    for j in range(i+1):
        if j!=i:
            print(' ',end=' ')
        else:
            print(j+1, end=' ')
    print()

'''


for i in range(1,5):
    
    for j in range(1):
        print((i-1)*' ',i,end='')
    print()




x = 'delhi'
for i in range(5):
	for j in range(5):
		if i>=j:
			print(x[j], ' ', end = '')
		else:
			print('   ', end ='')
	print()

	



x = 'delhi'
for i in range(5):
	for j in range(5):
		if i+j ==4:
			print(x[j], ' ', end = '')
		else:
			print('   ', end ='')
	print()




x = 'delhi'
for i in range(5):
	for j in range(5):
		if i+j <=4:
			print(x[i], ' ', end = '')
		else:
			print('   ', end ='')
	print()




x = 'delhi'
for i in range(5):
    for j in range(5):
        if i + j >= 4:
            print(x[i+j-4],' ',end=' ')
        else:
            print('   ',end=' ')
    print()




x = 'delhi'
res = ''
for i in range(len(x)):
    res += x[i]
    print(" "*(len(x)-len(res)), end ='')
    print(res)

'''

n = int(input('enter the no. of rows to print: '))
x = 1
for i in range(n):
    for j in range(n):
        if(j<=i):
            print(x," ",end = " ")
            x = x+1
    print("")




print("enter 2 numbers below")
a = int(input("enter number1:"))
b = int(input("enter number2:"))
ch=0
while ch<5:
    print("calculator menu")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
 

    #input choice
    ch= int(input("enter choice(1-5):"))

 

    if ch==1:
        c= a+b
        print("sum=", c)
    elif ch==2:
        c= a-b
        print("difference=", c)
    elif ch==3:
        c= a*b
        print("product=",c)
    elif ch==4:
        c= a/b
        print("quotient=",c)
    elif ch==5:
        break
    else:
        print("invalid choice")





for i in range(5):
	if i==3:
		break
	print(i)
print('ok')




for i in range(5):
	if i==3:
		break
	print(i)
print(i)




for i in range(5):
	if i == 3:
		continue
	print(i)
print(i)




for i in range(3):
	for j in range(3):
		if j==2:
			break
		print(j)





for i in range(3):
	for j in range(3):
		if j==2:
			continue
		print(j)




x = 4
if x>3 or x<6 and x==7:
	print('ok')
else:
	print('hi')





x = "dwarka"
for i in x:
    print(i)

    
    
    
x = 'dwarka'
l = len(x)
for i in range(l):
	print(x[i])    
   
    
    
    
    
x = input('enter a str:')
for i in x:
	print(i)  



#to print the length of a word
x = input('enter:')
c = 0

for i in x:
	c = c+1
print(c)    


    
    
    
# to print number of vowels in a sentence    
x = input('enter: ')
a=0
for i in x:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        a+=1
    else :
        a=a
print(a)

    
    
    
    
for i in x.lower():
    #if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
    if i in 'aeiou':
        a+=1
    else :
        a=a
print('Vowels are',a)





s = input("enter ")
a = 0
for i in s:
    if(i == " "):
        print(a)
        a = 0
    elif(i in "aeiouAEIOU"):
        a+=1
print(a) 

    
    
    

x = input('Enter a word')
for i in range(-1, -len(x)-1, -1):
	print(x[i], end = ' ')




x = 'dwarka'
for i in range(-1,-7,-1):
	print(x[i], end = ' ')





x = 'dwarka'
print(id(x[0]))





#Program to print no. of each vowel

vowels = 'aeiou'
x = input('Enter Sentence - ')
x = x.casefold()
count = {}.fromkeys(vowels,0)
for i in x:
   if i in count:
       count[i] += 1
print(count)





x = 'dwarka'
for i in range(5,-1,-1):
	print(x[i], end=' ')




x = 'amazing'
print(x[-1:-8:-1])





x = 'dwArkafghvgfdwarka'
print(x.find('war'))
print(x.find('war', 1, 4))
print(x.find('war', 2, 4))
print(x.find('war', 3, 4))




x = '!#%'
print(x.isalnum())

x = 'dps123@'
print(x.isalnum())

x = 'dpadwarka'
print(x.isalnum())






x = 'ewdkl'
print(x.isalpha())

x = 'DPS@@'
print(x.isupper())




x = 'DPS DWARKA'
print(x.lower())
print(x)




x = '  dps123  '
print(x.lstrip())
print(x)



x = 'dps123'
print(x.lstrip('d'))

print(x)





while True:
	print('0. Exit')
	print('1. Add')
	print('2. Sub')
	x = int(input('enter choice: '))
	if x==0:
		break
	elif x==1:
		print('Addition')
	elif x ==2:
		print('hello')
	else:
		print('valid input not entered')






x = '123123d'
print(x.isdigit())
print(x.isnumeric())






x = input('Enter a sentence: ')
print(x.capitalize())





x=input("enter: ")
y=''
lt='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for j in range(len(x)):
	for g in range(len(lt)):
		if x[j]==lt[g]:
			y=y+lt[g]
		elif x[j]==' ':
			y=y+x[j]
			break
print(y)






x = 'today is thursday'

for i in x:
	if i == ' ':
		print()
	else:
		print(i, end='')





x = 'awerty'
a = chr(65)
 
print(a)






x = input('Enter a sentence')
for i in range(len(x)):
	print(i)






x = input('Enter a sentence: ')
y =''
for i in range(len(x)):
	if i==0:
		y = y+x[i].upper()
	elif x[i-1] == ' ':
		y = y+x[i].upper()
	else:
		y = y+x[i]
print(y)








x = input('Enter a sentence: ')
y =''
for i in range(len(x)):
	if i== (len(x)-1):
		y = y+x[i].upper()
	elif x[i+1] == ' ':
		y = y+x[i].upper()
	else:
		y = y+x[i]
print(y)







a=[0]
for i in a:
     print(i)
     a.append(i+1)






for i in range(1, 11):
	print(i,end=' ')
print()
for i in range(2,21,2):
	print(i, end =' ')







for i in range(10,1,-1):
	print(i,end=' ')
print()
for i in range(20,2,-2):
	print(i, end=' ')








x = int(input('Enter a number: '))
for i in range(1,11):
	print(x,' * ', i ,' = ', x*i)






i=0
while i < 5:
	print('dps')
	i=i+1
	
	





i = 1
while i <= 10:
	print(i, end = ' ')
print()
i = 2
while i <= 20:
	print(i, end = ' ')
	i = i+2
	
x = int(input('ferfe: '))

i = 1
while i<=10:
	print(x, '*', i, '=', x*i)
	i = i+1







for i in range(5):
	for j in range(2):
		print('1')
		



a=1
b=1
print(a, b, end=' ')
for i in range(5):
	c = a+b
	print(c,end = ' ')
	a=b
	b=c




x = 123
print(x%10)






x = int(input('Enter a number: '))
s=0
while x>0:
	y=x%10
	s=s+y
	x=int(x/10)
print(s)







for i in range(3):
	for j in range(3):
		print('1', end = ' ')
	print()






x = 'delhi'
for i in range(5):
	for j in range(5):
		print('1', end=' ')
	print()






x = 'delhi'
for i in range(5):
	for j in range(5):
		print(x[i], end=' ')
	print( )

print()

x = 'delhi'
for i in range(5):
	for j in range(5):
		print(x[j], end=' ')
	print()

print()

x = 'delhi'
for i in range(5):
	for j in range(5):
		if i==j:
			print(x[j], end=' ')
		else:
			print(' ', end=' ')
	print()

print()

x = 'delhi'
for i in range(5):
	for j in range(5):
		if i>=j:
			print(x[i], end=' ')
		else:
			print(' ', end=' ')
	print()
	
print()

x = 'delhi'
for i in range(5):
	for j in range(5):
		if i>=j:
			print(x[j], end=' ')
		else:
			print(' ', end=' ')
	print()








x = 'delhi'
for i in range(5):
	for j in range(5):
		if i+j>=4:
			print(x[j], end=' ')
		else:
			print(' ', end=' ')
	print()







print()


x = 'delhi'
for i in range(5):
    for j in range(5):
        if i + j >= 4:
            print(x[i+j-4],' ',end=' ')
        else:
            print('   ',end=' ')
    print()








x='delhi'
for i in range(5):
    for j in range(5):
        if i>=j:
            print(x[i+j-4],' ',end=' ')
        else:
            print('   ',end=' ')
    print()








x = int(input('Enter no. 1: '))
y = int(input('Enter no. 2: '))
z = int(input('Enter no. 3: '))
if x>y and x>z:
	print('x is greatest')
elif y>x and y>z:
	print('y is greatest')
elif z>y and z>x:
	print('z is greatest')
else:
	print('All are equal')







x = input('Enter trafic signal(r/y/g): ')
if x=='r' or x=='R':
	print('Stop')
elif x == 'y' or x=='Y':
	print('Ready')
elif x == 'g' or x=='G':
	print('Go')
else:
	print('Invalid Input')






x = input('Enter trafic signal(r/y/g): ')
if x in 'rR':
	print('Stop')
elif x in 'yY':
	print('Ready')
elif x in 'gG':
	print('Go')
else:
	print('Invalid Input')








x = input('Enter trafic signal(r/y/g): ')
if x== 'r' or 'R':
	print('Stop')
elif x == 'y' or x=='Y':
	print('Ready')
elif x == 'g' or x=='G':
	print('Go')
else:
	print('Invalid Input')








x = int(input('Enter your age :'))
if x>0 and x<=5:
	print('Infant')
elif x>5 and x<=20:
	print('Teen')
elif x>20 and x<=60:
	print('adult')
else:
	print('Senior Citizen')









x = int(input('Enter a number: '))


if x%5 == 0:
	print('Yes, it is divisible. ')
else:
	print('No, it is not divisible')







x = 7%-3
print('7%-3',' ',x)

y = -7%-3
print('-7%-3',' ',y) 

z = 7%3
print('7%3',' ',z)

a = -7%3
print('-7%3',' ',a)








print(*range(10))








x = int(input('Enter a number: '))
for i in range(1, 11):
	print(x, 'x', i, '=', x*i )








x = 0
while x<=5:
	print(x, end = ' ')
	x = x+1
print('\nDone',x)


for i in range(6):
	print(i, end = ' ')
print('\nDone',i)






x="Hello"
X="How are you?"
print(x)
print(X)






x = int(input('Enter age: '))
if x>0 and x<=18:
	print('kid')
elif x>18 and x<=60:
	print('Adult')
else:
	print('Senior Citizen')






x = int(input('Enter Your Age: '))
if 0<x<=18:
	print('Kid')
elif 18<x<=60:
	print('Adult')
else:
	print('Senior Citizen')






# 1^2 + 2^2 +...
x = int(input('Enter Range'))
s = 0
for i in range(1,x):
	s = s+i**2
print(s)






#1*x + 2*x^2 + 3*x^3 + ......

x = int(input('Enter a  number: '))
n = int(input('Enter number of terms: '))
s=0
for i in range(1,n+1):
	s = s+i*x**i
print(s)






# x + x/2 + x/3 + .....
x = int(input('Enter a  number: '))
n = int(input('Enter number of terms: '))
s = 0
for i in range(1,n+1):
	s = s+(x/i)
print(s)







# 1+ 1/2 + 1/3 + 1/4+......
s=0
for i in range(1,n):
	s=s+1/i
print(s)







# x + x^2/2 + x^3/3 + ....
x = int(input('Enter'))
s = 0
for i in range(1,n):
	s = s+(x**i)/i
print(s)






# Factorial(!)
x = int(input('Enter a number: '))
s = 1
for i in range(x,0,-1):
	s = s*i
print(s)







# 1 + x^1/1! + x^2/2! + x^3/3! + ....
x = int(input('Enter a no.: '))
n = int(input('Enter a number: '))
t = 1
for j in range(1,n):
	s = 1
	for i in range(j,0,-1):
		s = s*i
	t = t+(x**i)/s
print(t)







# 1-2+3-4+5-....
n = int(input('Enter no. of terms: '))
s = 0 
for i in range(1,n):
	if (i%2!=0):
		s = s+i
	else:
		s = s-i
print(s)







# 1 + x^1/1! + x^2/2! + x^3/3! + ....
x = int(input('Enter a no.: '))
n = int(input('Enter a number: '))
t = 1
for j in range(1,n):
	s = 1
	for i in range(j,0,-1):
		s = s*i
		if (i%2!=0):
			t = t+(x**i)/s
		else:
			t = t-(x**i)/s
print(t)






while True:
	print('\t\t\t\tMenu')
	print('\t\t\t1. Area of Square')
	print('\t\t\t2. Area of Rectangle')
	print('\t\t\t3. Area of Circle')
	print('\t\t\t4. Exit')
	c = int(input('Enter your Choice[1/2/3/4]: '))
	if c==1:
		s = int(input('Enter Side of square: '))
		a = s*s
		print('Area of Square is: ',a)
	elif c==2:
		s = int(input('Enter Length of rectangle: '))
		b = int(input('Enter Breadth of Rectangle: '))
		a = s*b
		print('Area of Rectangle is: ',a)
	elif c==3:
		s = int(input('Enter Radius of Circle: '))
		a = 3.14*s**2
		print('Area of Circle is: ',a)
	else:
		break
print('Loop Ended')







for i in range(4):
	for j in range(4):
		print('1',end = ' ')
	print()









for i in range(4):
	for j in range(4):
		if i>=j:
			print('1', end=' ')
		else:
			print(' ', end = ' ')
	print()


for i in range(4):
	for j in range(0,i+1):
		print('1', end=' ')
	print()







for i in range(1,5):
	for j in range(1,5):
		if i<=j:
			print(j, end=' ')
		else:
			print(' ', end = ' ')
	print()








for i in range(1,5):
	for j in range(1,5):
		if i+j<=4:
			print(j, end=' ')
		else:
			print(' ', end = ' ')
	print()







#1
#2 3
#4 5 6
#7 8 9 10
k = 1
for i in range(1,5):
	for j in range(1,5):
		if i>=j:
			print(k, end=' ')
			k = k+1
		else:
			print(' ', end = ' ')
	print()







#A
#B C
#D E F
#G H I J
n = int(input('Enter the number of rows: '))
c = 'A'
x = 65
for i in range(n):
    for j in range(i+1):
        print(chr(x),end = " ")
        x+=1
    print()







#A
#B C
#D E F
#G H I J
k = 65
for i in range(1,5):
	for j in range(1,5):
		if i>=j:
			print(chr(k), end=' ')
			k = k+1
		else:
			print(' ', end = ' ')
	print()








x = int(input('Enter a decimal number: '))
s = ''
while True:
	if x>0:
		s = s + str(x%2)
		x = x//2
	else:
		break
print(s)
print(s[::-1])






#Factorial ofa number
x = int(input('Enter a number: '))
s=1
for i in range(x,0,-1):
	s = s*i
print(s)








while True:
	print('\t\t\t\t\tMENU')
	print('\t\t\t\t1. Armstrong Number ')
	print('\t\t\t\t2. Prime Number ')
	print('\t\t\t\t3. Special Number ')
	print('\t\t\t\t4. Automorphic Number ')
	print('\t\t\t\t5. Exit ')
	c = int(input('Enter choice: '))
	if c == 1:
	
		x = int(input('Enter a number: '))
		y = x
		s = 0
		while True:
			if x>0:
				s = s+((x%10)**3)
				x = x//10
			else: 
				break
		if s==y:
			print('IT IS AN ARMSTRONG NUMBER.')
		else:
			print('IT IS NOT AN ARMSTRONG NUMBER.')

	elif c == 2:


		x = int(input('Enter a number: '))
		flag = 0
		for i in range(2,x):
			if x%i == 0:
				flag = 1
		if flag == 0:
			print('IT IS A PRIME NUMBER.')
		else:
			print('IT IS NOT A PRIME NUMBER.')


	elif c == 3:
		x = int(input('Enter a number: '))
		y = x
		t = 0
		while True:
			if x>0:
				q = x%10
				s = 1		
				for i in range(q,0,-1):
					s = s*i
				t = t+s
				x = x//10
			else: 
				break
		if t==y:
			print('IT IS A SPECIAL NUMBER.')
		else:
			print('IT IS NOT A SPECIAL NUMBER.')
	
	elif c == 4:
		x = int(input('Enter a number: '))
		y = x**2

		if y>=0 and y<100:
			z = y%10
		elif y>=100 and y<1000:
			z = y%100
		elif y>=1000 and y<10000:
			z = y%1000	
		if z==x:
				print('IT IS AN AUTOMORPHIC NUMBER.')
		else: 
				print('IT IS NOT AN AUTOMORPHIC NUMBER.')

	
	
	elif c == 5:
		break
	else:
		print('ENTER A VALID INPUT.')
		
		
		
		



x = 'dwarka, is in, new delhi India'

print(x.find('New', 16,19))







x = [1,2,3,4]
print(x)







x = list('hello')
print(x)






# will give error
x = list(1234)
print(x)







x = list('dps dw')
print(x)







x = 'dps dw'
s = x.split()
print(s)






x = 'good, morning india'
s = x.split(',')
print(s)







x = list(input('Enter a value: '))
print(x)







x = input('Enter a value: ')
s = x.split()
print(s)










x = [1,2,3]
y= [1,2,3]
z =x+y
print(z)



x = [1,2,3]
y= [1,2,3]
z =x+y
print(z)




x = [1,2,3]
print(x*3)







# will give error
x = [1,2,3]
print(x+3)







l1 = [1,2,3]
l1[0]=10
print(l1)







x = [1,2,3,4]
y = x
x[0] = 10
print(x)
print(y)










x = [1,2,3,4]
y = list(x)
x[0] = 10
print(x)
print(y)






x = [1,2,3,4]
y = x
y[0] = 10
print(x)
print(y)






x = [1,2,3,4]
y = x

print(id(x))
print(id(y))

x[0] = 10

print(id(x))
print(id(y))






x = [1,2,3,4]
y = list(x)

print(id(x))
print(id(y))

x[0] = 10

print(id(x))
print(id(y))








x= 10
y = x
print(id(x))
x = 20
print(id(x))







x = [1,2,3,4]

print(id(x))
print(id(x[0]))

x[0] = 10
y = 10
print(id(x))
print(id(x[0]))
print(id(y))






x = [1,2,3]

x.append(6)
print(x)






x = [1,2,3]
y = [4,7,2]
x.extend(y)
print(x)







x = [1,2,3]
y = [4,5,6]
x.append(y)
x.extend(y)
print(x)






x = [1,2,3]
y = [4,5,6]

x.extend([1,2,3,4,5])
print(x)









x =[1,2,3]
y = [4,6,5]
x.insert(1,10)
print(x)






x =[1,2,3,4]
y = [4,6,5]
x.insert(-1,10)
print(x)







x =[1,2,3,4]
y = [4,6,5]
x.insert(len(x),10)
print(x)







x =[1,2,3,4]
y = [4,6,5]
x.insert(len(x),10)
print(x)









x = [1,2,3,4]
print(x)
y = x.pop()
print(x)
print(y)








x = [1,2,3,4]
print(x)
y = x.pop(2)
print(x)
print(y)






x = [1,2,3,4]
print(x)
y = x.pop(-2)
print(x)
print(y)





x = [1,2,3,4]
print(x)
y = x.remove(2)
print(x)






x = [1,2,3,4,2,2,2,2]
print(x)
y = int(input('Enter the no.: '))
y = x.remove(2)
print(x)







x = [1,2,3,4,2,2,2,2]

print(x)
while True:
	try:
		x.remove(2)
	except:
		print(x)
		break









x = ['d', 'p','s']
x.reverse()
print(x)







x = ['d', 'x','s']
x.sort()
print(x)







x = ['d', 'x','s']
x.sort(reverse = True)
print(x)






l = []
N = int(input('Enter no. of Words: '))
for i in range(N):
	x = input('Enter String: ')
	l.append(x)
L=[]
for i in l:
	i = list(i)
	i.sort()
	a = ''.join(i)
	L.append(a)
l=L
print(l)









s = 'Today is Thursday'
l = s.split()
print(l)








l = ['Today', 'is', 'Thursday']
q = '' #this joins everything in one go, put a space or something, it joins q with l using whatever is provided in q
q = q.join(l)
 
print(q)








while True:
x = []
print('\t\t\tMenu')
print('1. Add Elements')
print('2. Modify Elements')
print('3. Delete Elements')
print('4. Sort list')
print('5. Display')
print('6. Exit')
c = int(input('Enter the choice: '))
	if c == 1:
		x = list(input('Enter the list: '))
		y = int(input('Enter the position at which: '))







#accepts integer list & size is determined by user

x = []
while True:

	y = int(input('Enter elements: '))
	x.append(y)
	c = input('Continue(y/n): ')
	if c=='n':
		break
print(x) 











x = []
c = int(input('Enter list size: '))
for i in range(c):

	y = int(input('Enter elements: '))
	x.append(y)
	
	
print(x) 









x = []
c = int(input('Enter list size: '))
for i in range(c):

	y = int(input('Enter elements: '))
	x.append(y)
z = input()
	
print(x) 








x = input('Enter a word: ')
s = ''
l = len(x)
for i in range(l-1,-1,-1):
	s = s+x[i]

print(s)
if x == s:
	print('Yes')
else:
	print('Not')





x = int(input('Enter 1 no. : '))
y = int(input('Enter 2 no. : '))
z = int(input('Enter 3 no. : '))
if x>y and x<z or x>y and x<z:
	print('Second highest no. is', x)
elif y>x and y<z or y<x and y<z:
	print('Second highest no. is', y)
elif z>y and z<x or z>y and z<x:
	print('Second highest no. is', z)
else:
	print('Numbers are equal')





x = 1
s = 0
for i in range(5):
	print(x)
	s = s+x
	x = s+x
	print(s)








x = input('Enter a word: ')
y = input('Enter another word: ')
s = ''
for i in range(len(x)):
	s = s + x[i] + y[i]
print(s)








def binasc():
	x = []
	q = int(input('Enter no. of elements in list: '))
	for i in range(q):
		z = int(input('Enter no. in list: '))
		x.append(z)
	l = 0
	
	s = int(input('Enter the no. to search: '))

	while l <= q-1:
		m = (l+q-1)//2
		if s==x[m]:
			print('Element Found at location: ',m)
			break
		elif s<x[m]:
			l=m+1
		else:
			m = m-1
	else:
		print('Element not found')
while True:
	print('\t\t\t\tBinary Search')
	print('\t\t\t1.In Ascending Order')
	print('\t\t\t2.In Decending Order')
	print('\t\t\t3.Exit')
	w  = int(input('Enter choice: '))
	if w==1:
		binasc()
	elif w==2:
		bindesc()
	else:
		break







x = 10
y = 20
print(x,y)
t = x
x = y
y = t

print(x,y)





x = 10
y = 20
print(x,y)
x,y = y,x
print(x,y)



x=int(input())
for i in range(x):
	n = i%10
	
	for j in range(n):
		print(i)



x = {0:'abc', 2:'pqr', 3:'xyz'}
print(x)
print(x[1])
print(x[1][1])




#insertion sort dessc
x = [5,6,13,22,3,2,55]

for i in range(1,len(x)):
	t = x[i]
	j = i-1
	while j >= 0 and t > x[j]:
		x[j+1] = x[j]
		j  = j-1
		
	else:
		x[j+1] = t
print(x)




#insertion sort asc
# correct it
x = [5,6,13,22,3,2,55]

for i in range(1,len(x)):
	t = x[i]
	j = i+1 b
	while j >= 0 and t < x[j]:
		x[j-1] = x[j]
		j  = j+1
		
	else:
		x[j-1] = t
print(x)		






#Bubble sort desc
x = [1,4,2,7,8,9]

t = 0
for i in range(5):
	for j in range(5):
		if x[j]< x[j+1]:
			t=x[j]
			x[j] = x[j+1]
			x[j+1] = t
print(x)  



#Bubble sort asc
x = [1,4,2,7,8,9]

t = 0
for i in range(5):
	for j in range(5):
		if x[j]> x[j+1]:
			t=x[j]
			x[j] = x[j+1]
			x[j+1] = t
print(x) 







def Sort_Tuple(x):
	y = len(x)
	for i in range(0, y):
		for j in range(0, y-i-1):
			if (x[j][-1] > x[j+1][-1]):
				z = x[j]
				x[j]= x[j+1]
				x[j+1]= z
	return x
	
x = eval(input('Enter the nested tuple: '))
		
print('Sorted tuple is: ', Sort_Tuple(x))




p = tuple()

q = int(input('Number of elements: '))

for i in range(q):

   y = int(input('Enter number: '))

   p += (y,)

print('stored tuple is: ', p)








x = [(45, 23, 12), (7, 8), (22, 14, 3)]
print('The original tuple is : ', x)
y = 0
for i in x:
	for j in i:
		y = y + j
z = y/len(x)
print('The mean is : ', z)
'''














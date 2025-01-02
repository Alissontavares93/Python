# First challenge
'''nome=input('Por favor digite seu nome:\n')
print('Ola, e um prazer te conhecer, ',nome,'!')'''

#Secund challenge (Primitive types)
'''n1=int(input('Digite um numero:\n'))
n2=int(input('Digite mais um numero\n'))
s=(n1+n2)
print()
print('the sum between {} and {} is {}'.format(n1,n2,s))'''

'''name=input('Whats your name? ')
print(name.isalpha())
print(len(name)==0)'''

#Tests with strings
'''algo=input('Insert something: ')
print('This date is of the type: ', type(algo))
print('Are all spaces?: ',algo.isspace())
print('all are alphabetics? ',algo.isalnum())
print('all are lowercase? ',algo.islower())'''

#Test with strings II
'''algo=input('Insert something: ')
if not algo.isalnum():
    print('Attention! Your password needs to have just letters and numbers uppercase and lowercase.')
elif algo.islower():
    print('Attention! Your password needs to have at least one uppercase letter')
else:
    print('Done! Please wait..')'''

#Exercises 

#01
#Show the predecessor and the successor of the a number.
'''n1=int(input('enter a number: '))
pre=n1-1
suc=n1+1                                                                     
print('The predesessor is {} and the successor is {}.'.format(pre,suc))'''        

#02
#Calculate and show the double, the triple, and the root square.
'''N=int(input('Enter a integer number: '))
D=N*2
T=N*3                                             
SR=N**0.5
print('The double is {}, the triple is {}, and the root square is {:.2f}'.format(D,T,SR))'''

#3
#calculates the everage
'''n1=float(input('Enter the first note: \n'))
n2=float(input('Now enter the secund note: \n'))          
M=(n1+n2)/2
print('The avarage between {} and {} is {:.2f}'.format(n1,n2,M))'''

#4
#Convert from meter to centimeter and millimeter.
'''S=float(input('Enter a value in meters:\n'))
cm=S*100
mm=S*1000                                                               
print('This value corresponds to ({})cm, and ({})mm'.format(cm,mm))'''

#5
#Calculate multiplication tables.
'''N=int(input('Enter a number:'))
for i in range(1, 11):
    R=N*i                                                               
    print(f'{N} x {i} = {R}')'''

#6
#Convert any amount from real to US dollar.
'''V=int(input('How much do you have?(R$)\n'))                          
D=V*6,17
print('{:.2f} R$ corresponds to {}USD (01/01/25.)'.format(V,D))'''        

#7
#Calculates the size in square meters of a wall and informs you how much paint is needed to paint it.
'''W=float(input('Whats the Width of the wall?(m)\n'))
H=float(input('Now enter the Height(m)\n'))
paint=int(input('What is the yield per liter of paint?(m2)\n'))
T=W*H                                        #Total in cm2    
y=(1/paint) * T                                  #Vol L
print(f'Your total area is {T}m, and the amount of paint needed to paint is {y}L.')'''

#8
#Calculates the new value of a product with the discount defined by the user.
'''CurPrice=float(input('Whats the current price?(xx.xx)'))
disc=float(input('Enter whats discount value: (xx.xx%)'))
red=(CurPrice*disc)/100
new_price=CurPrice-red
print('The new value with discount is {:.2f}'.format(new_price))'''

#9
#15% Increase
current_salary=float(input('Enter your current salary:(xxx.xx)'))
new_salary=1.15*current_salary
print('Your new salary is {:.2f}.'.format(new_salary))
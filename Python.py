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
n1=int(input('enter a number: '))
pre=n1-1
suc=n1+1
print('The predesessor is {} and the successor is {}.'.format(pre,suc))


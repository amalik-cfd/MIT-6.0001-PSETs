# AS = int(input("Enter your annual salary:  "))
# PC = float(input("Enter the percentage of your salary to save, as a decimal: "))
# Cost = int(input('Enter the cost of your dream home: '))
# SAS = float(input('Enter the semi-annual salary raise: '))
# Current_savings = 0
# Down_payment = 0.25*Cost
# r = 0.04
# i = 0
# while Current_savings<=Down_payment:
#       Current_savings = Current_savings + ((PC*AS)+(Current_savings*r))/12
#       i+=1
#       n=i%6
#       if n == 0:
#           AS = AS + SAS*AS         
#       else:
#           AS = AS
#       print(Current_savings, i)
# years = i//12      
# months = i%12
# if months == 0:
#     print('Your downpayment will be saved in', years,'years')
# else:
#     print('Your downpayment will be saved in', years,'years and',months,'months')
# #print('Your downpayment will be saved in', i,)

import sys
AS = int(input("Enter your annual salary:  "))
MS = AS/12.0
#PC = float(input("Enter the percentage of your salary to save, as a decimal: "))
Cost = 1000000
# SAS = float(input('Enter the semi-annual salary raise: '))
Current_savings = 0
Down_payment = 0.25*Cost
r = 40
i = 0
k = 0
l = 0
h = 10000
PC = 0 
while abs(Current_savings-Down_payment)>100:
    MS = AS/12.0
    Current_savings = 0
    for i in range(37):
        n=i%6
        if n == 0:
            MS+=0.07*MS
        else:
            MS = MS
        Current_savings += ((PC*MS)+(Current_savings*r))/10000.0
    if Down_payment-Current_savings > 100:
        l = PC
    elif Current_savings - Down_payment > 100:
        h = PC        
    else:
        break
    PC = (h+l)//2
    k +=1
    if k > 13:
        print('It is not possible to save the downpayment in three years')
        sys.exit()
PC = PC/10000.0
print('Best savings rate:',PC)
print('Steps in bisection search:',k)

# for i in range(37):
#        n=i%6
#        if n == 0:
#            MS+=0.07*MS
#        else:
#            MS = MS
#        Current_savings += (PC*MS)+(Current_savings*r)
# print(Current_savings)


# years = i//12      
# months = i%12
# if months == 0:
#     print('Your downpayment will be saved in', years,'years')
# else:
#     print('Your downpayment will be saved in', years,'years and',months,'months')
#print('Your downpayment will be saved in', i,)



















####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# i = 0
# while i < len(word):
#     char = word[i]
#     if char in an_letters:
#         print("Give me an " + char + "! " + char)
#     else:
#         print("Give me a  " + char + "! " + char)
#     i += 1
# print("What does that spell?")
# for i in range(times):
#     print(word, "!!!")

#cube = int(input('give a number: '))
# for g in range(abs(cube)+1):
#     # print(g)
#     if g**3 >= abs(cube):
#        break
# if g**3 != abs(cube):
#     print('no integer cube root')
# else:
#     if cube < 0:
#         g = -g
#     print('cube root of',cube,'is',g)
# e = 0.1
# g = 0.00
# i = 0.01
# n = 0
# while abs(g**3-cube)>=e and g<=cube:
#     print(g)
#     g+=i
#     n+=1
# print(n, 'guesses')
# if abs(g**3-cube)>=e:
#     print('fail')
# else:
#     print(g,'is close to the cube root of',cube)
# import matplotlib.pyplot as plt
# n = int(input('the number of zeroes: '))
# m = [0]*n
# k= [0]*n
# for i in range(n):
#     k[i] = 10**i
#     e = 0.01
#     n = 0
#     l = 0
#     h = k[i]
#     g = (l+h)/2.0
#     while abs(g**3-k[i])>=e:
#         if g**3<k[i]:
#             l = g
#         else:
#             h = g
#         #print(g)
#         g = (h+l)/2.0
#         n+=1
#     #print('for',cube,'num of guessses is', n)
#     #print(g, 'is close to the cube root of', cube)
#     m[i] = n
#     #print(m)
# #print(m)
# print(k)
# plt.plot(k,m)
# plt.ylim(1,100)
# print(k[n-2])
# plt.xlim(0,k[n-2])
# plt.show()


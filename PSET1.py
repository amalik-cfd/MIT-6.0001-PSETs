# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:11:37 2022

@author: User
"""
#Dream home cost
# print('PART A: House Hunting.')
# print('Please enter your dream home cost.')
# total_cost = float(input())
# print('Please enter your annual salary.')
# annual_salary = float(input())
# print('How much portion of your salary would you like to save?')
# portion_saved = float(input())*annual_salary/12
# portion_down_payment = 0.25 * total_cost
# current_savings = 0
# r = 0.04
# i = 0
# while current_savings <= portion_down_payment:
#     investment_returns_monthly = current_savings*r/12
#     current_savings = current_savings + investment_returns_monthly + portion_saved
#     i = i + 1
# print(i, 'months')

# print('PART B:Saving with a raise.')
# print('Please enter your dream home cost.')
# total_cost = float(input())
# print('Please enter your annual salary.')
# annual_salary = float(input())
# print('How much portion of your salary would you like to save?')
# saving_pc = float(input())
# print('How much is your semi annual raise?')
# semi_annual_raise = float(input())
# portion_down_payment = 0.25 * total_cost
# current_savings = 0
# r = 0.04
# for i in range(0,1000,1):
#     if i % 6 == 0 and i!=0:
#         annual_salary = semi_annual_raise*annual_salary + annual_salary    
#     print(annual_salary, i)
#     portion_saved = saving_pc*annual_salary/12
#     investment_returns_monthly = current_savings*r/12
#     current_savings = current_savings + investment_returns_monthly + portion_saved
#     if current_savings >= portion_down_payment:
#         break
# print(i+1, 'months')

# The goal is to able to afford a down payment in say three years.  How much should I save each month to achieve 
# this 

print('PART C:Finding the right amount to save.')
#print('Please enter your dream home cost.')
#total_cost = 1000000.00
print('Please enter your annual salary.')
k = float(input())
#print('How much portion of your salary would you like to save?')
#saving_pc = float(input())
#print('How much is your semi annual raise?')
semi_annual_raise = 0.07
portion_down_payment = 250000
current_savings = 0
r = 0.04
sp = 5000
epsilon = 100
low = 0
high = 10000
n =0
while abs(current_savings - portion_down_payment) >= epsilon:
    current_savings = 0
    portion_saved = 0
    annual_salary = k
    for i in range(0,37,1):
        if i % 6 == 0 and i!=0:
            annual_salary = semi_annual_raise*annual_salary + annual_salary       
        portion_saved = sp*annual_salary/120000
        investment_returns_monthly = current_savings*r/12
        current_savings = current_savings + investment_returns_monthly + portion_saved
    if current_savings < portion_down_payment:
        low = sp
    else:
        high = sp
    sp = (high + low)/2

    if n > 100:
        print('It is not possible to pay down payment with',k)
        break
    n+=1
print('The savings rate is',sp/10000.0,'the number of guesses is', n)
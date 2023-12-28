# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:03:16 2023

@author: Malik.Huzaifa
"""


# def printMove(x, y):
#     print('move from ' + str(x) + ' to ' + str(y))
    

# def Towers(n, fr, to, spare):
#     if n == 1:
#         printMove(fr, to)
#     else:
#         Towers(n-1, fr, spare, to)
#         Towers(1, fr, to, spare)
#         Towers(n-1, spare, to, fr)


# Towers(2, 'P1', 'P2', 'P3')

# def t(x):
#     if x == 1:
#         print('end')
#     else:
#         t(x-1)
    
#     return print('lol',x)
# t(3)

# def f(n):
#     print(n)
#     if n==1:
#         print('end')
#         return 1
#     elif n==2:
#         print('end2')
#         return 2
#     else:
#         return f(n-1)+f(n-2)
    

# f(4)

# def palin(s):
#     def tochars(s):
#         s =s.lower()
#         ans = ''
#         k = 'abcdefghijklmnopqrstuvwxyz'
#         for c in s:
#             if c in k:
#                 ans = ans+c
#         print(ans)
#         return ans
#     if len(s)==0 or len(s)==1:
#         print('palindrome')
#     elif tochars(s)[0]==tochars(s)[-1]:
#         palin(tochars(s)[1:-1])
#     else:
#         print('not a palindrome')
    
# k=str(input('please type out a word:\n'))
# palin(k)
# def lyrics_to_frequencies(lyrics):
#     myDict = {}
#     for word in lyrics:
#         if word in myDict:
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
#     return myDict
    
    
# she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
# 'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

# 'you', 'think', "you've", 'lost', 'your', 'love',
# 'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
# "it's", 'you', "she's", 'thinking', 'of',
# 'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

# 'she', 'says', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'she', 'said', 'you', 'hurt', 'her', 'so',
# 'she', 'almost', 'lost', 'her', 'mind',
# 'and', 'now', 'she', 'says', 'she', 'knows',
# "you're", 'not', 'the', 'hurting', 'kind',

# 'she', 'says', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',

# 'you', 'know', "it's", 'up', 'to', 'you',
# 'i', 'think', "it's", 'only', 'fair',
# 'pride', 'can', 'hurt', 'you', 'too',
# 'pologize', 'to', 'her',

# 'Because', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'Yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'yeah', 'yeah', 'yeah',
# 'yeah', 'yeah', 'yeah', 'yeah'
# ]

# beatles = lyrics_to_frequencies(she_loves_you)
# def commons(freqs):
#     values = freqs.values()
#     best = max(values)
#     words=[]
#     for k in freqs:
#         if freqs[k]==best:
#             words.append(k)
#     return(words,best)
# def words_often(freqs, minTimes):
#     result = []
#     done = False
#     while not done:
#         temp = commons(freqs)
#         if temp[1] >= minTimes:
#             result.append(temp)
#             for w in temp[0]:
#                 del(freqs[w])  #remove word from dict
#         else:
#             done = True
#     return result
def fib_eff(n,d):
    if n in d:
        #print('here')
        return d[n]
    else:
        #print('alsohere')
        ans = fib_eff(n-1, d)+ fib_eff(n-2, d)
        d[n] = ans
        return ans
d = {1:1,2:2}
fib_eff(10,d)
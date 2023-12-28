# import string
# t = 'Purple cow'
# t = t.lower()
# t = t.split()
# ans = []
# for k in yes_check_list:
#     for i in k:
#         if i in string.punctuation:
#             k = k.replace(i,' ')
#     k = k.lower()
#     list = k.split()
#     print(list)
#     emp = []
#     for word in t:
#         # print(word)
#         if word in list:
#             emp.append(word)
#             # print(emp)
#     ans.append(emp == t)
#     print(ans)
# no_check_list = ['Purple cows are cool!',
#  'The purple blob over there is a cow.',
#  'How now brown cow.',
#  'Cow!!! Purple!!!',
#  'purplecowpurplecowpurplecow']

# yes_check_list = ['PURPLE COW',
#  'The purple cow is soft and cuddly.',
#  'The farmer owns a really PURPLE cow',
#  'Purple!!! Cow!!!',
#  'purple@#$%cow',
#  'Did you see a purple cow?']

# import string
# t = 'Purple cow'
# t_1 = t.lower()
# t_2= t_1.split()
# t_3 = t_1.replace(' ','')
# ans = []
# for k in yes_check_list:
#     print(type(k))
#     for i in k:
#         print(i)
#         if i in string.punctuation:
#             k = k.replace(i,' ')
#     k = k.lower()
#     list = k.split()
#     print(list)
#     emp = ' '.join(list)
#     for word in list:
#         if word not in t_2:
#             emp = emp.replace(word,'?',1)
#     emp = emp.replace('?','')
#     emp = emp.strip()
#     print(emp)
#     ans.append(emp == t_1)
#     print(ans)

phrase = 'purple cow'
text = 'The purple cow is soft and cuddly.'
text = 'Purple!!! Cow!!!'
def is_phrase_in(phrase,text):
    phrase = phrase
    text = text.lower()
    phrase_list = phrase.split()
    if text == phrase:
        return True

    for letter in text:
        if letter in string.punctuation:
            text = text.replace(letter,' ')
    text_list = text.split()
    emp = ' '.join(text_list)
    for word in text_list:
        if word not in phrase_list:
            emp = emp.replace(word,'?',1)
    emp = emp.replace('?','')
    emp = emp.strip()
    return emp == phrase


is_phrase_in(phrase,text)
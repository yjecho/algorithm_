#!/usr/bin/python
# -*- coding: latin-1 -*-

# my_name = 'alex'

# # print(my_name[2])

# my_name[2] = 'p'
# print(my_name)

# customer_id = 'alex@hphk.kr'

# splitted_list = customer_id.split('@')
# print(splitted_list)

# a = 'h'
# b = 't'
# print(a+b)

from tracemalloc import stop


customer_id = 'alex@hphk.kr'

real_id = ''

for letter in customer_id:
    if letter != '@':
        real_id += letter
    elif letter == '@':
        break

print(real_id)

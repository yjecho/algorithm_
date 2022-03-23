# !/usr/bin/python
# -*- coding: latin-1 -*-

word = 'level'

# reverse_word = word[::-1]
# print(reverse_word)

# for num in range(3, -1, -1): # 3:-1 거꾸로볼래-1 = 3.2.1.0 
#     print(num)

# for num in range(len(word)-1,-1,-1):
#     print(num)

reverse_word = ''

for idx in range(len(word)-1,-1,-1):
    reverse_word += word[idx]

print(reverse_word)

if word == reverse_word:
    print("It's palindrome!")
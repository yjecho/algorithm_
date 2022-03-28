#!/usr/bin/python
# -*- coding: latin-1 -*-

# 기초 자료들
# cards = [8,3,2,8,1,8]

# 바를정자를 그릴 틀을 만들자
# 0,1,2,3,4,5,6,7,8,9 - 1~9
# 0,1,1,1,0,0,0,0,3,0 - 숫자의 개수
# cards_count = [0,0,0,0,0,0,0,0,0,0]

# for num in cards:
#     cards_count[num] += 1
#     # 첫번째 8 -> 인덱스 8+1=9 -> cards_count의 9번째에 1을 기입해서 새로운 값으로 해줘
# print(cards_count)

# for cnt in cards_count:
#     # 새로 생성된 리스트 [0, 1, 1, 1, 0, 0, 0, 0, 3, 0] 에서 3이 있는지 확인
#     if cnt >= 3:
#         print('triplet founded')

cards = [4, 8, 7, 3, 1, 5, 5, 6]

card_counts = [0]*10

for num in cards:
    card_counts[num] += 1

is_run = False

for i in range(len(cards)-2):
    if card_counts[i] >= 1 and card_counts[i+1] >= 1 and card_counts[i+2] >=1:
        is_run = True

print(is_run)

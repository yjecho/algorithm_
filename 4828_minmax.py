# 3 - TC 전체 개수
# 5 - 1st tc
# 477162 658880 751280 927930 297191
# 5 - 2nd tc
# 565469 851600 460874 148692 111090
# 10 - 3rd tc
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

# input 함수가 7번 먹이 달라고 함


# 문제

# [입력]

# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# T = int(input()) # 첫 번째 라인 끝 (=3)

# for tc in range(1, T+1): # 즉, for tc in range(1,4):
#     N = int(input()) # 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 ) : "5,5,10은 N이다."
#     nums = list(map(int, input().split())) # 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 ) : 숫자들을 받겠다.

#     answer = 0
#     # 문제 로직이 들어감

#     # 최종 출력 예시
#     print('#{} {}'.format(tc, answer))


# 상동
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    answer = max(nums) - min(nums)

    # 최종 출력 예시
    print('#{} {}'.format(tc, answer))



# 실습
# T = int(input())

# for tc in range (1, T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     answer = max(nums) - min(nums)

#     print(f'#{N}: {answer}')

# 기초 - 각 케이스의 합은?
# 3
# 1 2 3
# 5 6 7 8 1 2
# 4 4 3 2 1 1

# T = int(input())

# for tc in range(1, T+1):
#     nums = list(map(int, input().split()))
#     answer = sum(nums)

#     print('#{}: {}'.format(tc, answer))
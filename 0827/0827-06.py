# # 조건문 안에 조건문
# a = 76
# if a>50:
#     if a<100:
#         print("50보다크고 100보다작은 수")
#     else:
#         print("50보다크고 100보다 큰 수")
# else:
#     print("50조다 작은 수")


# 조건문을 여러개 쓸때
# score = 65
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("E")

# import random
# random_no = random.randint(-10,10)
# print("랜덤숫자",random_no)

# if random_no>0:
#     print("양수")
# elif random_no=0:
#     print("0입니다.")
# else:
#     print("음수")

# import random
# score = random.randint(0,100)
# if score>=60:
#     print("합격")
# elif score>=50:
#     print("재시험")
# else:
#     print("불합격")
# print("랜덤점수 : ",score)

# 랜덤점수를 생성해서
import random
# 90이상 A, 80점이상 B, 70-C, 60-D, 나머지는 F
score = random.randint(0,100)
# 랜덤점수를 출력하지오.
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")
# print("랜덤점수",score)

# 90-92 A-, 93-97 A, 98 A+
# 80-82 B-, 83-87 B, 88 B+
# 70-72 C-, 73-77 C, 77 C+
# 60-62 D-, 63-67 D, 66 D+
# 랜덤점수를 출력하세요.
# if score>=90:
#     if score>97:
#         print("A+")
#     elif score>92:
#         print("A")
#     elif score<=92:
#         print("A-")
# elif score>=80:
#     if score>87:
#         print("B+")
#     elif score>82:
#         print("B")
#     elif score<=82:
#         print("B-")
# elif score>=70:
#     if score>77:
#         print("C+")
#     elif score>72:
#         print("C")
#     elif score<=72:
#         print("C-")
# elif score>=60:
#     if score>67:
#         print("D+")
#     elif score>62:
#         print("D")
#     elif score<=62:
#         print("D-")
# else:
#     print("F")
# print("랜덤점수",score)

# if : 조건문
# if
# if -else
#if elif else
#if elif elif else
# if 조건문:
#   들여쓰기 되어야 함
# else:
#   들여쓰기가 되어야 함
# if 조건:
#   공백일때 pass로 가능하다.
# else:
# if 10>5 : prit("ok") 한줄 가능, 명령이 여러개일때에는 반드시 및에 들여쓰기 한다.
# else:

import datetime
now = datetime.datetime.now()

# 해당월에 따라 봄, 여름, 가을, 겨울로 출력하시오

# mont = now.month
mont = int(input("월입력 하시오>>"))
if 11>=mont>=9:
    print("가을입니다.")
elif 8>=mont>=6:
    print("여름입니다.")
elif 5>=mont>=3:
    print("봄입니다.")
elif mont==12 or mont<=2:
    print("겨울입니다.")
else:
    print("잘못 입력하였습니다.")
print("랜덤수 : ",mont)

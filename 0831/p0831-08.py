# 1~100사이의 랜덤번호를 맞추는 프로그램을 구현하시오
# 랜덤번호 보다 입력값이 높으면 낮은수를 입려하시오!, 낮으면 높은수를 입력하시오!
# 정답을 맞추면
# 정답숫자 :
# 숫자입력 횟수 :
# 입력한 숫자 :

import random
lan_num = random.sample(range(1,100),6)
my_no = []
count = 0
while True:
    xx = input("숫자를 입력하시오(프로그램 종료 'x') >> ")
    if xx=="x":
        break
    else:
        no=int(xx)
        my_no.append(no)
        count = count+1
    if no>lan_num:
        print("낮은수를 입력하세요!")
    else:
        print("높은수를 입력하세요!")

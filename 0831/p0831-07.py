# mynum = []
# # for i in range(6):
# #     no = int(input("숫자입력 : "))
# #     if no not in mynum:
# #         mynum.append(no)
# #     else:
# # #         print("입력한 숫자가 있습니다.")
# # # print("입력한 숫자 : ",mynum)
# # i = 0
# # while i=6:
# #     no = int(input("숫자입력 : "))
# #     if no not in mynum:
# #        mynum.append(no)
# #        i = i+1
# #     else:
# #         print("이미 숫자가 있습니다.")
# #     
# # print("입력한 숫자 : ",mynum)

# import random
# lotto = random.sample(range(1,46),6)
# my_num = []

# # print("로또번호 : ",lotto)
# print("로또번호 : ",lotto)

# # 6개를 입력받아 있는지 확인하시오.
# while i=6

# # 로또번호 :
# # 정답번호 :
# # 정답갯수 :

import random

# 로또 랜덤부분
lotto = random.sample(range(1,46),6)

# 6개 입력부분
myNum = []  # 6개 입력
i = 0
while i<6:
    no = int(input("숫자입력 : "))
    if no > 45:
        print("잘못입력 하셨습니다.")
    elif no not in myNum:
        myNum.append(no)
        i = i+1
    else:
        print("번호가 있습니다.")

# 정답확인 부분
answer = []
count = 0
for i in myNum:
    if i in lotto:
        count = count + 1
        answer.append(i)
print("맞춘번호 갯수 : ",count)
print("로또번호 : ",lotto)
print("맞춘번호 : ",answer)
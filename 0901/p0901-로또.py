# no = "13"
# if no.isdigit(): # 문자열의 숫자변환 유무 확인
#     print(no)

import random

# 로또 랜덤부분
lotto = random.sample(range(1,46),6)

# 6개 입력부분
myNum = []  # 6개 입력
i = 0
while True:
    i = i+1
    if i == 6:
        break
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
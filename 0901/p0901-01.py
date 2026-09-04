# 구구단
for i in range(2,9+1):
    for j in range(1,10):
        print("{}x{} = {}".format(i,j,i*j))

# 1-100사이의 숫자맞추기
# 1. 랜덤번호 1개
import random
ran_num = random.randint(1,100)

# 2. 숫자를 무한으로 입력받기
arr = []
in_no = 0 # 입력변수
while True:

# 3. 숫자를 입력받기
    in_no = int(input("1-100사이의 수 입력 : ")) # 숫자입력 받기
    arr.append(in_no)
# 4. 숫자 비교
    if in_no == ran_num:
        print("정답입니다.")
        break
    elif in_no > ran_num: # 입력한수가 크면
        print(in_no,"보다 작으수를 입력하세요.")
    else:
        print(in_no,"보다 큰수를 입력하세요")
print('"축" 당첨입니다.')
print("랜덤숫자 : ",ran_num,"\t입력한 숫자 : ",in_no)
print("입력한 횟수 : ",len(arr))
print("입력한 모든 수 : ",arr)



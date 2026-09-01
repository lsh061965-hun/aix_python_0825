# break : 반복문을 환전 동료
# continue : 1번만 제외 이후 계속 반복

# for i in range(100):
#     if i%2==0:
#         continue
#     print(i)    

# no = []
# name = []
# i = 1
# while True:
#     n = input("{}.이름입력 : ".format(i))
#     name.append(n)
#     no.append(i)
#     if n == "0": break
#     i = i + 1

# print("프로그램 종료.")


# 1~100까지 랜덤숫자 1래를 생성

# import random
# ran_num = random.randint(1,10)   # 랜덤숫자
# my_num = 0                       # 내가 입력한 수
# my_list = []
# while True:
#     my_num = int(input("1~10까지의 숫자입력>>"))
#     print(my_num)
#     my_list.append(my_num)
#     if my_num == ran_num:
#         print("정답입니다.")
#         break
#     elif my_num>ran_num:
#         print("입력한 수가 큽니다.")
#     else:
#         print("입력한숫자가 작습니다.")
# print("입력한 숫자 : ",my_list)
# print("프로그램 종료")



# ranNo = [1,5,9,7,4]
# inputNo = [1,2,3,4]
# answerNo = []
# # 입력한 숫자와 랜덤숫자와 몇개가 맞는지 개수를 출력하시오.
# count = 0
# for i in inputNo:
#     if i in ranNo:
#         count = count + 1
#         answerNo.append(i)
#         print("있음")
#     else:
#         print("없음")

# print("개수 : ",count)

# 1~100까지 랜덤숫자 1개를 생성
# 내가 입력한 모든 숫자가 출력
# 랜덤숫자를 맞출때까지 무한반복 프로그램을 구현하시오.
# import random
# randNum = random.randint(1,100) # 랜덤숫자생성
# my_list = []    # 입력한숫자모두저장
# myNum = 0       # 내가입력한숫자변수
# answer = 0      # 정답변수
# while True:
#     myNum = int(input("1-100사이 숫자를 입력 : "))
#     my_list.append(myNum)

#     # 랜덤숫자와 입력숫자가 같은지 비교
#     if myNum == randNum:
#         answer = myNum
#         print("정답입니다.")
#         break
#     elif myNum>randNum:
#         print("입력한 숫자가 더 큽니다. 작은수 입력!!")
#     else:
#         print("입력한 숫자가 더 작습니다. 큰수 입력!!")

# print("정답 : ",answer)
# print("정답 : ",my_list[-1])
# print("입력한모든 숫자 : ",my_list)

# print("프로그램 종료")




# # break : 반복문 완전 종료
# # continue : 1번만 제외 이후 계속 반복
# no = []
# name = []
# i = 1  #번호
# while True:
#     n = input("{}.이름입력 : ".format(i))
#     if n == "0": break

#     name.append(n)
#     no.append(i)
#     i = i + 1

# print("프로그램 종료")





# for i in range(100):
#     if i==50:
#         break
#     print(i)

# print("프로그램 종료")

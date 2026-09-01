# for i in range(10):
#     print(i)

# i = 1
# while(i<11):
#     print(i)
#     i += 1     # 조건식이 참일때만 반복한다.

# # 모든 for문은 while로 변경이 가능하다. 서로 변경이 가능
# # for : 반복, 구간지정
# # while : 조건식이 있을때, 무한반복할때

# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# print("-"*50)
# i = 1
# while(i<11):
#     print(i)
#     i += 2

# 모든 for문은 while변경 가능함.
# for : 반복, 구간지정 1-10까지
# while : 조건식이 있을때, 주로 사용, 무한반복일때 사용

# i = 0
# while True:
#     print(i)
#     i += 1

# alist = list(range(10))

# # while 문을 사용해서 alist 있는 값을 출력하시오.
# # 0 1 2 3 4 5 ...9

# i = 0     # 초기값
# while i < 10:  # 조건식
#     print(alist[i],end=" ")
#     i += 1    # 증감식 
# # 초기값, 조건식, 증감식 이 반드시 필요함

# l = ["바나나","달기","사과"]
# i = 0
# while i < 3:
#     print("{}:{}".format(i,l[i]))
#     i += 1

# i = 0
# while True:   # True:무한 반복
#     if i%10==0:
#         print(i)
#         inp = input("프로그램을 종료할까요?")
#         if inp == "x":
#             break
#     i += 1

# break(for, while)을 종료시켜줌.

a = 0
b = 0
while True:
    a = int(input("1.숫자 >>"))
    if a==0: break
    b = int(input("2.숫자 >>"))
    if b==0 : break
    print("{} + {} = {}".format(a,b,a+b))
print("프로그램 종료")


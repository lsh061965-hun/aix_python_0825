# for i in range(10):  # 1,2,3,4,5,6,7,8,9,
#     print(i)
# for i in range(1,6):
#     print(i)
# print("-"*10)
# for i in range(0,11,2):
#     print(i)
# name = []
# for i in range(3):
#     na = input("이름을 입력하시오>>")
#     name.append(na)
# print(name)


# 이름입력을 3번 반복하시오.
# name = []
# for i in range(3):
#     a = input("이름입력 : ")
#     name.append(a)  # 리스트:append,insert,extend

# print("[ 학생명단 ]")
# print(name)
# for n in name:
#     print(n)
# [ 학생명단 ]
# 홍길동
# 유관순
# 이순신


# for i in range(3): # 0,1,2
#     print(i)

# for i in range(1,6):
#     print(i)
# print("-"*10)
# for i in range(1,11,2):
#     print(i)

# nums = [3,9,10,105,220,2,1]
# for n in nums:
#     print(n)

# 3:홀수
# 9:홀수
# 10:짝수

# 입력한 숫자가 홀수인지,짝수인지 출력하시오.
# a = int(input("숫자입력 : "))
# %2==0
# nums = [3,9,10,105,220,2,1]
# for nu in nums:
#     if nu%2==0:
#         print(nu," : 짝수입니다.")
#     else:
#         print(nu," : 홀수입니다.")

# for 변수 in " " >> 에는 범위(range(1,11,2)) 리스트 문자도 가능하다.  매우 중요하다.

# print(1)
# print(2)
# print(3)
# print(4)
# print(1,end="")  # end="" 샆입시 옆으로 출력된다.
# print(2,end=" ")
# print(3,end="\t")
# print(4)


# 구구단 출력
for i in range(2,10):
    print (i,"X",1, "=", i*1)
    print("{} X {} {}".format(i,1,i*1))
    print


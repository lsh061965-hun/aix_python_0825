# rum1 = 100
# rum2 = 200
# rum3 = 300
# print(rum1, rum2, rum3)

# num4=num5=num6=1  # 한줄에 여러값을 넣는것은 가능
# print(num4, num5, num6)

# a1=1, a2="안녕"  # 서로다른 변수는 한줄에 넣을 수 없다.
# a1=1
# a2="안녕"
# print(a1, a2)

# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b) # a의 b승을 말함

# print : 출력
# input : 입력

# num = input("숫자를 입력하세요")
# print("입력숫자 : {}".format(num))

# input로 입력받은 모든것은 문자열타입으로 인식한다.
# a = int(input("첫번째 숫자를 입력하세요."))   # str타입을 int타입으로 변경
# b = int(input("두번째 숫자를 입력하세요."))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)

# 아이디, 패스원드를 입력받아 출력하시요.
# 아이지 : aaaa , 패스워드 : 1111

# a = "aaa"
# b = 222
# id = input("아이디 :")
# pw = input("패스워드 :")
# print("아이디 : {}".format(a==id))
# print("패스워드 : {}".format(b==pw))


# 출력되도록 하시오.
# 잔액 : 1000
# 송금금액 : 100
# 총금액 1100

# a = 1000
# b = int(input("송금액을 입력하시오 :"))
# inp0 = (a + b)
# print("총 잔액 : {}".format(inp0))

# c = int(input("인출액을 입력하시오 :"))
# out0 = (inp0 - c)
# print("총 잔액 : {}".format(out0))



# 국어, 영어, 수학점수를 입력받아 
# 합계, 평균을 출력하시오.

# name = input("이름을 입력하세요 :")
# kor = int(input("국어점수 입력 :"))
# eng = int(input("영어점수 입력 :"))
# math = int(input("수학점수 입력 :"))

# total = (kor + eng + math)
# ag = (total / 3)

# print("수험자 이름 : {}".format(name))
# print("합계점수 : {}".format(total))
# print("평균점수 : {:.2f}".format(ag))


# a,b = 1,2
# print(a,b)   # 가능한 작업
             
# a = b = 1
# print(a,b)   # 가능한 작업

# a = 1, b = 2
# print(a, b)   # 불가능한 작업


# 수를 2진수로 변환하는 명령어 "bin()"이다.
# print(bin(5))   # 0b101 앞의 0b는 이진수임을 나타냄

# print(int("101",2))  # 이진수를 10진수로 바꾸는 법


# a = 9
# b = 2

# print(a/b)    # 실수
# print(a//b)   # 몫
# print(a%b)    # 나머지

# 짝수, 홀수 구분법
a = int(input("숫자를 립력하시오 :"))
print(a%2==1)
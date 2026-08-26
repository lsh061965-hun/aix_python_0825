#  연산자 : 숫자열, 문자열 연산자가 따로 있다.
#  산술 연산자 : +, -, *, /, //, %, **
# 산술연산은 *, / 먼저 +, - 순으로 함


# print(2+2-2*2/2*2)
# print(2+2-((2*2)/2)*2)
# print(2-2+2/2*2+2)

# # 문자열연산은 +, *(반복 연결기능을 함)만 가능 
# print("안녕" + "하세요")  # +는 연결 연산자
# print("안녕" * 10)       # *는 반복 연삱자

# # 문자열 숫자인경우 솟자타입으로 변경가능

# str1, str2, str3 = "100", "1.1234", "999"
# # print(str1 + 1)  # 불가능 
# print(int(str1)+1)   # 문자열 숫자를 정수형으로 변경함
# print(float(str2))     # 문자열 숫자를 실수형으로 변환
# print(int(str3)+1)

# 번호, 이름, 국어, 영어, 수학을 입력받아
# 번호, 이름, 국어, 영어, 수학, 합계, 평균을 출력하세요.


# num = input("순서입력 : ")
# nam = input("이름입력 : ")
# kor = int(input("국어점수 입력 : "))
# eng = int(input("영어점수 입력 : "))
# mat = int(input("수학점수 입력 : "))
# total = (kor + eng + mat)
# eg = (total / 3)
# print("-" * 110)
# print("순서 : {}\t 이름 : {}\t 국어 : {}\t 영어 : {}\t 수학 : {}\t 합계 : {}\t 평균 : {:.2f}"\
#       .format(num, nam, kor, eng, mat, total, eg))
# print("-" * 110)
# # print("국어 : {}, 영어 : {}, 수학 : {}".format(kor, eng, mat))
# # print("합계 : {}, 평균 : {:.2f}".format(total, eg))


# print("101"+"102")  # 101102
# print("안녕"+"하세요")  # 안녕ㅎ하세요

# a = 10
# a = a +2
# a += 2
# print(a)  # 같은형식으로 출력 됨


# 원의 바지름을 입력받아
# 원의 넓이를 출력하시오
length = int(input("바지름을 입력하세요."))
pi = 3.14
result = pi * (length ** 2)
result2 = 2 * pi * length
print("원의 넓이 : ", result)
# print("원의 넓이 : {}".format(pi * (length**2)))
print("원의 둘래 : {:.2f}".format(result2))
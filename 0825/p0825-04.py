# 변수 : 값을 저장하는 공간, 타입은 값을 입력할때 정해진다.
# 타입 : 정수, 실수, 문자, 불스타입이 있다.

# a = 10    # 숫자형의 정수타입
# b = 10.1  # 숫자형의 실수타입(소수점)
# c = "안녕" # 문자열 타입
# d = true   # 불타입(bool) - true, false / boolean

# 예약어는 변수로 사용할 수 없음.
# true = 1
# print = 5

# print(10+5)
# print(10-5)
# print(10*5)
# print(10/5)
# print(10//5)  # 몫 2
# print(10%5)   # 나머지 0
# print(10**5)  # 제곱 100,000

# 입력값이 바뀔때(변수를 사용하여 프로그래밍을 한다.)

# a = 10
# b = 5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)  # 몫 2
# print(a%b)   # 나머지 0
# print(a**b)  # 제곱 100,000

# 변수타입 확인 

a = 100
b = 10.1
c = "문자"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 위의 내용을 출력시 결과내용은 아래와 같다.
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
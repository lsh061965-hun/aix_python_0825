# str1 = "안녕"  #문자열
# int1 = 1      #숫자-정수형
# float1 = 1.1  #숫자-실수형
# bool1 = True  #불형

# # 리스트 - 모든타입이 들어올수 있음(리스트안에 리스트가능)
# arr = [str1,int1,float,bool1,[1,2,3,"안녕"]]

# # 자료형 확인 - thpe()
# print(thpe(float1))

# thpe 변경 : int()-정수, float()-실수, str()-문자, bool()-블타입
str2 = "111"
str3 = int(str2)
print(str2)   
print(type(str2))
print(int(str3))
print(type(str3))

# 문자열 선언 - "", ''
# ""를 출력하고 싶을때 \를 넣으면 뒤에있는것을 문자로 인식
print("안녕 나는 \"홍길동\"이라고 해.")
print('안녕 나는 "홍길동"이라고 해.')
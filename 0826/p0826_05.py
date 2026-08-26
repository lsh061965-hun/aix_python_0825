# # 산술연산자 +,-,*,/,//,%,**

# money = 12340
# # 500원 동전 몇개가 필요할까?

# result = money // 500   # 500동전 갯수
# num = money % 500
# result2 = num // 100  # 100동전 갯수
# num2 = num % 100
# result4 = num2 // 10   # 10동전갯수

# print("500동전 필요갯수 : ", result)
# result0 = money // 100
# print("100동전 필요갯수(전체) : ", result0)
# print("100동전 필요갯수 : ", result2)
# print("10동전 필요갯수 : ", result4)


# 관계연산자 ==, !=, >, <, >=, <=
# True, False의 bool타입으로 반환한다.

# a = 10
# b = 5
# print(a==b)  # False
# print(a!=b)  # True
# print(a>b)   # True
# print(a<b)   # False


# 아이디, 패스워드를 임력받아 맞는지 확인
a = "aaa"
b = 1111

id = input("아이디를 입력하세요>>")
pw = input("패스워드를 입력하세요>>")

if(id=="aaa") and (pw=="1111"):  # 참이면 다음실행(둘다 참일때)
  print("정상적으로 동짝합니다.")
else:                             # 거짓이면 다음실행(둘중 하나라도 거짓이면)
  print("잘못된 정보입니다.")

if(id=="aaa") or (pw=="1111"):  # 둘중 하나라도 참이면 다음동작
  print("사용 가능 합니다.")
else:                           # 둘다 거짓이면 다음동작
  print("다시 시도하세요.")

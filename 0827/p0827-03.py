# 입력한 숫자가 양수인지 음수인지 출력하시오.
# 1.숫자입력 2.양수,음수 비교 3. 출력

# a = int(input("숫자입력 : "))
# if a>0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")

# # 입력한 수가 2의 배수인지 아닌지 확이 출력
# b = int(input("숫자를 입력>>"))
# if b%2 == 0:
#     print("2의 배수")
# else:
#     print("2의 배수가 아님")

# 산술연산자 : +,-,*,/,//,%,**
# 비교연산자 : ==,!=, >,<,>=,<=
# 논리연산자 : and, or, non이 있다.

# 랜덤함수
import random # 파이선에 있는 random클래스 사용하겠다 선언
# randint(1,100) # 1부터 100까지중 랜덤으로 숫자 결정
num = random.randint(1, 5)
input1 = input("1~5까지의 숫자를 입력하시오>>")
print("랜점숫자 : ", num)
print("이력한 숫자 : ", input1)
if (num==input1):
    print("당첨")
else:
    print("꽝")
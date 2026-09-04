# c,자바 : 컴파일 언어--> 전체를 기계어로 번역
# 파이썬 : 스크립티 언어--> 한줄씩 기계어 번역
# 한수는 ()있으면 99%하수이다.
# drf 이름(): 함수선언
# 호출은 이름()의 형식으로 한다. == 실행시킨다.
# 함수사용 이유 : 코드 재사용, 코드 간결
def d_print1():
    for i in range(1,10):
        print(i)

def hello_print():
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")

def cal(m1.n2):
    r1 = n1+n2
    r1 = n1-n2
    r1 = n1*n2
    r1 = n1/n2
    return r1,r2,r3,r4

d_print1()  # 호출하면 실행한다.
hello_print()
n1 = int(input("1.숫자입력 : "))
n2 = int(input("2.숫자입력 : "))

r1,r2,r3,r4 = cal(n1,n2)

print(r1,r2,r3,r4)
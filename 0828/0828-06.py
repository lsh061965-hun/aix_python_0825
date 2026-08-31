# format함수
# a = 10
# print("{}".format(a))
# print("{:10d}".format(a))
# print("{:010d}".format(a))
# print("{:3,d}".format(a))
# print("{:.2d}".format(a))
# print("{:12.2f}".format(a))
# print("{:012.2f}".format(a))


# while(True):  # 반복문 
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")
#     if id == "aaa" and pw == "1111":
#         print("로그임성공! 메인으로 이동")
#         break
#     else:
#         print("잘못입력했습니다.")

# paper =  """네팔 대 홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
# 2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 이번 
# 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서 
# 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."""

# res1 = paper.find("홍수")   #find(검색내용,시작위치,종료위치)값을 같는다.
# print(res1)
# res2 = paper.rfind("홍수")
# print(res2)
# res3 = paper.count("홍수")
# print(res3)

# # in 연산자
# if "콧울" in paper:   # 방울과 콧물로 확인하기
#     print("있음")
# else:
#     print("없음")

# split() 구분자로 분리
str = "1,홍길동,100,80,99"
s = str.split(",")   # 리스트 문자열
n1 = int(s[2])
n2 = int(s[3])
n3 = int(s[4])
t = n1+n2+n3
eg = t/3
s.append(t)
s.append(eg)
print(s)
print("번호\t이름\t국어\t영어\t수학\t합계\t평 균")
print("-"*55)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2F}".format(*s))  # (*S)는 구조분해 할당한다.

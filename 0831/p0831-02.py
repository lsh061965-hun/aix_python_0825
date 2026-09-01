# # 구구단을 아래로 출력하시오.
# for gu in range(1,10):
#     for gu1 in range(2,10):
# #        print(gu"X",gu1,"=",gu*gu1,end="\t")
# #        print("{}X{}={}".format(gu,gu1,gu*gu1),end="\t")
#         print(gu1,"단",end="\t")
#         if gu1==gu1:
#             pass
#         else:
#             print("{}X{}={}".format(gu1,gu,gu*gu1),end="\t")
#     print()


# sum = 0
# result = 1
# for i in range(1,101):
#     sum = sum+i
#     # result = result*i
#     if sum>100:
#          print(i, ":", sum)
#          break   # for문을 강재종료 시킴


# sum = 0
# for i in range(1,101):  # 홀수의 합을 구하시오 renge(1,101,2)로 해결
#     if i%7 == 0:
#         print(i)
#         sum = sum + i
# print("합 : ",sum)

# inpt = 0
# inp = []
# for i in range(3):
#     inpt = int(input("숫자를 넣으세요>>"))
#     inp.append(inpt)
# print("입력값 : ",inp)
# print("입력합계 : {}".format(inp[0]+inp[1]+inp[2]))

# 입력한 첫번째 부터 두번째 숫자까지의 합을구하시오.
# sum = 0
# in1 = int(input("1.첫번째 수를 립력 : "))
# in2 = int(input("2.두번째 수를 립력 : "))
# for i in range(in1,in2+1):
#     if in1>in2:
#         in1,in2 = in2,in1 # in1이 in2보다 클때는 값을 서로 교환한다.
#     else:
#     sum = sum+i
#     print(sum,end="\t")
# print("합계 : ",sum)

# 구구단을 출력하시오.
# 숫자입력받아 입력한 숫자부터 출력한다.
# inp = int(input("몇단부터 시작 수>>"))
# inp1 = int(input("끝부분>>"))
# for i in range(inp,10)

# list_a = ["바나나","딸기","사과"]
# j = 0
# for i in list_a:
#     print(j,":",i) # 1:바나나, 2:딸기,3:사과
#     j = j+1
# for i, value in enumerate(list_a): # enumerate는 indes번호, 리스트값을 받아온다.
#     print(i+1,":",value)

# for i in range(3):
#     print(i+1,":",list_a[i])

# for i in range(1,4):
#     print(i)

name = []
kor = []
eng = []
mat = []
total = []
eg = []
for i in range(3):
    name.append(input("이름입력 : "))
    kor.append(int(input("국어범수 입력 : ")))
    eng.append(int(input("영어범수 입력 : ")))
    mat.append(int(input("수학범수 입력 : ")))
    total.append = kor+eng+mat
    eg.append = total/3

print("[학생성적]")
for i in range(len(name)):
print("name[i]\tkor[i]\teng[i]\tmat[i]\ttotal[i]\tteg[i]")

# name = []
# kor = []
# eng = []
# math = []
# total = []
# avg = []
# for i in range(3):
#     name.append(input("이름입력 :"))
#     k_input = int(input("국어점수입력 : "))
#     kor.append(k_input)
#     e_input = int(input("영어점수입력 : "))
#     eng.append(e_input)
#     m_input = int(input("수학점수입력 : "))
#     math.append(m_input)
#     total.append(k_input+e_input+m_input)
#     avg.append((k_input+e_input+m_input)/3)

# print("[ 학생성적 ]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t")
# print("-"*60)
# for i in range(len(name)):
#     print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\
# \t{total[i]}\t{avg[i]:.2f}")
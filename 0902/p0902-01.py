# # 1,25까지 리스트를 생성하고
# # 랜덤으로 리스트를 섞은 다음, 5개씩 2차원리스트를 만드시오.
# import random
# alist = list(range(1,26))
# random.shuffle(alist)
# alist2 = []
# for i in range(0,len(alist),5):
#     alist2.append(alist[i:i+5])  #0,1,2
# for i in range(len(alist))
# print(alist2)

# # alist2 = [[],[],[],[],[]]



# # 문자열을 3자리씩 끊어서 리스트로 저장하시오.
# # aa = "abcdefabcdefabcdefabcdefabcdef" #30
# # aa2 = [] # 3개씩 나눠서 저장하시오.
# # for i in range(0,len(aa),3):
# #     aa2.append(aa[i:i+3])  #0,1,2
# # print(aa2)



# # 1차원리스트를 2차원형태로 구성
# # arr = [1,2,3,4,5,6,7,8,9]  #len(arr) = 9
# # arr2 = []
# # for i in range(0,len(arr),3):
# #     arr2.append(arr[i:i+3])  #0,1,2
# # print(arr2)

# # arr2 = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9],
# # ]


# 학생성적
stu = [
    # {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100},
    # {},
    # {}
]

# 화면출력
# 1. 성적입력
# 2. 성적출력
c_no = 1   #학생번호로 사용
while True:
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요."))
    # 학생성적 입력부
    if choice == 1:
        print()
        while True:
            print("[ 학생성적입력 ]")
            no = c_no
            name = input("학생이름입력 (0.이전페이지 이동) : ")
            if name=="0": break
            kor = int(input("국어점수입력 : "))
            eng = int(input("영어점수입력 : "))
            math = int(input("수학점수입력 : "))
            total = kor+eng+math
            avg = total/3
            stu.append(
                {"no":no,"name":name,"kor":kor,"eng":eng\
                ,"math":math,"total":total,"avg":avg}
            )
            print(name,"학생 성적이 저장되었습니다.")
            c_no += 1   # 다음번호 1증가
        print()
    # 학생성적 출력부
    elif choice == 2:
        print()
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\
\t{s['eng']}\t{s['math']}\t{s['total']}\
\t{s['avg']:.2f}")
        print()
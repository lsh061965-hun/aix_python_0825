# 학생성적
# stu = [
#     # {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100},
#     # {},
#     # {}
# ]

# 화면출력
# 1. 성적입력
# 2. 성적출력
# stu = []
# no = 1   #학생번호로 사용
# def main_print():
#     print("[ 학생성적프로그램 ]")
#     print("-"*60)
#     print("1. 학생성적입력")
#     print("2. 학생성적출력")
#     print("-"*60)
#     choice = int(input("원하는 번호를 입력하세요."))
# def stu_input():
#     if choice == 1:
#         print()
#         while True:
#             print("[ 학생성적입력 ]")
#             name = input("학생이름입력 (0.이전페이지 이동) : ")
#             if name=="0": break
#             kor = int(input("국어점수입력 : "))
#             eng = int(input("영어점수입력 : "))
#             math = int(input("수학점수입력 : "))
#             total = kor+eng+math
#             avg = total/3
#             stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
#             print(name,"학생 성적이 저장되었습니다.")
#             no += 1   # 다음번호 1증가
#             print()

while True:
    msin_print()
    # 학생성적 입력부
        stu_input()
    # 학생성적 출력부
    elif choice == 2:
        print()
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
            print()
    else:
        print("잘못 선택했습니다.")
        print()
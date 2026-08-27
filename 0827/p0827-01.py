# 학생 두명의 성적을 입력받아 출력하시오.
# 번호, 이름, 국어, 영어, 수학의 점수를 입력받아
# 번호, 이름, 국어, 영어, 수학의 순으로 출력하시오
num = input("번호를 입력하시오>>")
name = input("이름을 입력하시오>>")
kor = input("국어접수를 입력하시오>>")
eng = input("영어접수를 입력하시오>>")
mat = input("수학접수를 입력하시오>>")
total = (kor+eng+mat)
eg = (total/3)
print("-"*100)
print("번호 : {}, 이름 : {}\t 국어 : {}\t 영어 : {}\t 수학 : {}\t 합계 : {}\t 평균 : {:.2f}"\
      .format(num, name, kor, eng, mat, total, eg))
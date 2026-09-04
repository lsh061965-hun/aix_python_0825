# split 분리, *전개연산자
str = input("날짜를 입력하세요.(2026/09/02)")
str_arr = str.split("/")
print("{}년 {}월 {}일".format(*str_arr))
# 2026년 9월 2일



# # map, join -> 문자열
# stu = [1,"홍길동",100,100,100]
# stu = list(map(str,stu))   # map 특정한 함수로 반복해줌.
# # ,구분해서 문자열로 저장하시오.
# stu2 = ",".join(stu)
# print(stu2)



# # map(함수,반복리스트)
# aa = ['1','2','3']
# print(list(map(int,aa)))




# str = input("번호 3개를 입력하세요.(123/5/23) >> ")
# # 3개의 합을 구해서 출력하시오.
# strList = str.split("/")  #문자열타입
# strList = list(map(int,strList))  #문자열->정수타입으로 변환
# sum = 0
# for s in strList:
#     sum += s
# print(sum)


### 앞뒤공백제거 - strip()
a = "      abc       "
print(a.strip()) #공백제거 -> a반영은 안됨.

### 중간공백제거 - replace()
b = "     a      b"
print(b.strip())
print(b.replace(" ",""))

### 분리 : split - 리스트타입으로 전달됨.
c = "딸기,수박,바나나,사과"
print(c)
print(c.split(","))

d = "1,홍길동,100,100,100,300,100.0"
dlist = d.split(",")
dlist[2] = 90
dlist[3] = int(dlist[3])
dlist[4] = int(dlist[4])
dlist[5] = dlist[2]+dlist[3]+dlist[4]
dlist[6] = dlist[5]/3

dlist2 = [str(i) for i in dlist]
print(dlist)

# 특정문자로 결합 - join  "1"+1
# 문자열리스트만 변경가능 join결합
# 문자열로 변환됨.
d_str = ",".join(dlist2)
print(d_str)

# join
aa = "/"
bb = aa.join(["바나나","딸기","사과"])
print(bb)
print(type(bb))




# ss = "   파이썬"       #파이썬 - strip
# ss2 = "<<<<파<<이<썬"  #파이썬 -replace
# print(ss.strip())
# print(ss2.replace("<",""))


# aa = input("이름을 입력하세요.>> ").strip()

# aa = [1,2,   3, 4 ,5]




# ss = "파이썬 공부!! 열심히 합시다. 파이썬"
# print(ss.count("공부"))
# print(ss.count("파이썬"))
# print(ss.find("공부"))  #4
# print(ss.find("자바"))  #없을때 : -1
# print(ss.index("자바")) # index는 없을때 에러




# aa = "a/b/c/d/f/g"
# aa_list = aa.split("/")
# print(aa_list)

# bb = "100,10,5,4,1"
# # 모든수의 합을 구하시오.
# bb_list = bb.split(",")
# bb_list = [int(i) for i in bb_list]
# sum = 0
# for b in bb_list:
#     sum += b
# print(bb_list)
# print("합계 : ",sum)

# bb_list2 = [int(i) for i in bb_list]
# print(bb_list2)




# aa = "가나다라가가가나나다라라라라라라라"
# ##
# # {가:10,나:5,다:11...}
# aa_dict = {}
# for a in aa:
#     if a not in aa_dict:
#         aa_dict[a] = 1
#     else:
#         aa_dict[a] += 1


# print(aa_dict)



# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = []

# c = list(zip(a,b))
# d = dict(zip(a,b))
# print(c)
# print(d)

# for i,j in zip(a,b):
#     c.append([i,j])
# print(c)

# for i in range(len(a)):
#     c.append([a[i],b[i]])
# print(c)




# 리스트 생성방법
# a1 = [1,2,3,4,5]
# a2 = [0]*5
# a3 = list(range(1,6))
# a4 = [i*i+2 for i in range(1,6) if i%2==0] #리스트내포
# print(a4)


# # a = ["바나나","딸기","사과","딸기","딸기","사과"]
# aa = [1,2,3,1,1,1,2,3,1,1,1,2,2,3]
# # print(aa.count("딸기"))
# # {"바나나":1,"딸기":3,"사과":2}
# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else:
#         aa_dic[a] = aa_dic[a]+1
#         print("있습니다.")

# print(aa_dic)

# 딕셔너리
# a_dic = {"바나나":1,"딸기":3,"사과":2}
# print(a_dic["바나나"])  #출력
# a_dic["배"] = 5         #추가
# print(a_dic)
# del a_dic["바나나"]      #삭제
# print(a_dic)
# a_dic["사과"] = 100      #수정
# print(a_dic)

# a = 10
# a2 = 0
# a2 = a
# print(a2)
# a = 100
# print(a2)


# alist = [1,2,3]
# alist2 = []
# alist2 = alist      # 얕은복사
# # alist2 = [*alist] # 깊은복사
# print(alist2)  # 1,2,3


# alist[0] = 100
# print(alist2)

a = [1,2,3,4,5]
b = [10,20,30,40,50]
c = []





# 리스트 생성방법
# a1 = [1,2,3,4,5]
# a2 = [0]*5
# a3 = list(range(1,6))
# a4 = [i*i+2 for i in range(1,6) if i%2==0] #리스트내포
# print(a4)


# # a = ["바나나","딸기","사과","딸기","딸기","사과"]
# aa = [1,2,3,1,1,1,2,3,1,1,1,2,2,3]
# # print(aa.count("딸기"))
# # {"바나나":1,"딸기":3,"사과":2}
# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else:
#         aa_dic[a] = aa_dic[a]+1
#         print("있습니다.")

# print(aa_dic)

# 딕셔너리
# a_dic = {"바나나":1,"딸기":3,"사과":2}
# print(a_dic["바나나"])  #출력
# a_dic["배"] = 5         #추가
# print(a_dic)
# del a_dic["바나나"]      #삭제
# print(a_dic)
# a_dic["사과"] = 100      #수정
# print(a_dic)

# a = 10
# a2 = 0
# a2 = a
# print(a2)
# a = 100
# print(a2)


# alist = [1,2,3]
# alist2 = []
# alist2 = alist      # 얕은복사
# # alist2 = [*alist] # 깊은복사
# print(alist2)  # 1,2,3


# alist[0] = 100
# print(alist2)

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

# 1,25까지 리스트를 생성하고
# 랜덤으로 리스트를 섞은 다음, 5개씩 2차원리스트를 만드시오.
import random
alist = list(range(1,26))
random.shuffle(alist)
alist2 = []

# alist2 = [[],[],[],[],[]]



# 문자열을 3자리씩 끊어서 리스트로 저장하시오.
# aa = "abcdefabcdefabcdefabcdefabcdef" #30
# aa2 = [] # 3개씩 나눠서 저장하시오.
# for i in range(0,len(aa),3):
#     aa2.append(aa[i:i+3])  #0,1,2
# print(aa2)



# 1차원리스트를 2차원형태로 구성
# arr = [1,2,3,4,5,6,7,8,9]  #len(arr) = 9
# arr2 = []
# for i in range(0,len(arr),3):
#     arr2.append(arr[i:i+3])  #0,1,2
# print(arr2)

# arr2 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
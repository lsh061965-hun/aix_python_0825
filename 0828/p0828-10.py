# for i in range(3):
#     no = i+1
#     name = input("이름입력 : ")
#     print()

# for i in range(10):
#     print("안녕")

# for _ in range(10):
#     print("안녕")



# # for 변수 in 범위:
# for i in range(5):
#     print(i)

# for i in range(0,5):  
#     print(i*10)  

# for i in range(0,10,2):
#     print(i)  


# for i in [1,5,3,2]:
#     print(i)  

# for i in "안녕하세요":
#     print(i) 

# arr = list(range(1,11))          
# print(arr)

# 합계가 100이 넘어가는 시점은 몇번째 일까요?
sum = 0
# for i in range(1,11):
#     sum = sum+i
#     if sum>20:
#         print("100보다 클때 : ",i)
#         print("100이넘을때의 수 : ",sum)
#         break
#     else:
#         print("계속진행")

# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             print(i,j,k)
# for i in range(0,10):
#     for j in range(0,10):
#         print((i*10)+j+1,":",i,j,)

# 반복문을 이용하여 1-100까지 합을 출력하시오
tal = 0
for i in range(1,101):
    tal = tal+i
print(tal)

<<<<<<< HEAD
# 200을 엄는 시점의 i의 값과 i번째 합계를 출력하시오
=======
# 200을 얻는 시점의 i의 값과 i번째 합계를 출력하시오
>>>>>>> 8efa1702bab2548fa7d7c19ccd74897d4f857977
tal1 = 0
for i in range(1,101):
    if tal1>=200:
        print(i," :번째",tal1," :이다") 
        break      
    else:
        tal1 = tal1+i     

# 구구단을 출력하시오
for i in range(1,10):
    for j in range(1,10):
        print(i,"x",j,"=",i*j)

# 반복 입력 및 반복 출력을 할려면 list를 사용한다. 학생 성적 관리프로그램
stu = []
for i in range(2):
    no = 1+i
    name = input("이름을 입력하세요. : ")
    kor = int(input("국어점수 : "))
    stu.append([no,name,kor])
for i in range(2):
    print("{}\t{}\t{}".format(*stu[i]))

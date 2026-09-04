print("1.구구단 출력")
print("2.두수를 입력받아, +,- 값을 출력")
print("3. 1-10까지 합을 출력")
print()
choice = int(input("원하는 번호를 입력하세요.>> "))

def cal1():
    print()
    for i in range(2,10):
            for j in range(1,10):
                print(i,"x",j,"=",i*j)

def cal2():
    print()
    in_no1 = int(input("첫번째수 입력>>"))
    in_no2 = int(input("두번째수 입력>>"))
    print()
    print("두수의 합(+) : ",in_no1+in_no2,"두수의 뺄샘(-) : ",in_no1-in_no2)
    print()

def cal3():
    sum = 0
    for i in range(1,11):
        sum = sum+i
    print()
    print("1-10까지의 합은 : ",sum)

if choice == 1:
    cal1()
elif choice == 2:
    cal2()
else:
    cal3()
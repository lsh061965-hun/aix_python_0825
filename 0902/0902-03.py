str = input("번호 3개를 입력하세요.(123/5/23 >> )")
# 3개의 합을 구해서 출력하시오.
# str1 = str.replace("/",",")
# str2 = str1.split(",")
# str3 = 
# print(str1)
# print(str2)
strlist = str.split("/")
sum = 0
for s in strlist:
    sum += int(s)
print(sum)


# map함수(반복 > 리스트)
aa = [1,2,3,4,5]

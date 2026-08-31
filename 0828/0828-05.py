no = int(input("숫자 입력-->"))
str1 = input("인치를 넣으세요->")
str2 = int(str1)
bb = no*2.54
bb1 = str2*2.54
print("1입력값 : {}인치\t 2입력값 : {}인치".format(no, str2))
print("-"*46)
print("1입력값 : {:.2f}센치\t 2입력값 : {:.2f}센치".format(bb, bb1))
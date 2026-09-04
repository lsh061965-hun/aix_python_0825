# num_arr = [1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# stape = ["SPADE","HEART","DIAMOND","CLOVER"]
# aa = []
# # 아래와 같이 출력하시오.
# for s in stape:
#     for n in number:
#         aa.append([s,n])
#         # print("{}{}".format(s,n_arr[n-1]))
# random.shuffle(aa)
# print(aa)

# 딕셔너리 활용
stu_list = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
]


name_dic = {
    "aaa":'토마토',"ddd":"바나나","eee":"딸기","bbb":"배"
}

# import operator
# name_sort1 = []
# name_sort1 = sorted(name_dic.items(),key=operator.itemgetter(0))
name_sort1 = []
name_sort1 = sorted(name_dic.items(),key=lambda x:x[1])
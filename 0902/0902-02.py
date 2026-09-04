# alist = [1,2,3,2,3,2,3,2,3]
# # alist2 = []
# # alist2 = alist # 얕은복사() alist값이 바뀌면 alist2도 바뀐다.
# # alist2 = [*alist] # 깊음복사 상호간에 영향을 주지 않음

# alist.count(2)  # 키값의 갯수
# print(alist.count(2))

# # 리스트 생성 방법
# a1 = [1,2,3,4,5,6]
# a2 = [0]*5
# a3 = list(range(1,6))
# a4 = [i*i+2 for i in range(1,6) if i%2==0]  # 컴플래이션 또는 리스트 내포

# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = []
# for i in range(len(a)):
#     c.append(a[i]*b[i])
# print(c)
# for i,j in zip(a,b):
#     c.append([i,j])
#     print(c)

# c = list(zip(a,b))
# d = dict(zip(a,b)) 
# print(c)
# print(d)

# aa = "가나다라가가가나나다라라라라라라라"
# bb = {}
# for i in aa:
#     if i not in bb:
#         bb = bb+1



# ss = "   파이썬"         
# ss2 = "<<<<파<<이<썬"     # 둘다 파이썬으로 출력하시오
# print(ss.split())
# print(ss2.replace("<",""))

aa = "/"
bb


# lst = [12,3]
# nums = lst
# # val = lst
# del nums[:]
# # del lst
# print(lst)
# # print(lst)
# print(nums)
# # print(lst)
# print(val)



# def f1(x):
#     return None

# def f2(x):
#     return f1(x) * f1(x)

# print(f2(2))


# print(1//2)


# def f(a,b):
#     return b**a

# print(f(b=2,2))



# x=1
# y=2
# x,y,z = x,x,y
# z,y,z = x,y,z
# print(x,y,z)


x=3
y=2
x=x%y
x=x%y
y=y%x
print(y)



# x=1//5 + 1/5
# print(x)


# print("a","b","c",sep="sep")


# tupla = (1,2)
# tupla[1]=tupla[1]+tupla[0]
# print(tupla)


# lst=[i for i in range(-1,-2)]
# print(lst)




# def fun(a,b,c=0):
#     return 1

# print(fun(a=0,b=1))




# def fun(x,y):
#     if x==y:
#         return x
#     else:
#         return fun(x,y-1)

# print(fun(0,3))


# def fun(x):
#     if x%2==0:
#         return 1
#     else:
#         return 2

# print(fun(fun(2)))







# i=0
# while i<i+2:
#     i+=1
#     print("*")
# else:
#     print("*")








# dct={'uno':'dos','tres':'uno','dos':'tres'}
# v=dct['tres']

# for k in range(len(dct)):
#     v=dct[v]

# print(v)



# lst=[i for i in range(-1,-2)]
# print(lst)




# def fun(x,y):
#     if x==y:
#         return x
#     else:
#         return fun(x,y-1)

# print(fun(0,3))




# tup = (1,2,4,8)
# tup = tup[-2:-1]
# # val = tup[-2]
# tup = tup[-1]

# print(tup)


dct ={}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1],end="")

# a = 1<>0
# print(a)

# def f(a,b):
#     return a**a

# print(f(b=2),2)


# lst=[x*x for x in range(5)]
# def f(lst):
#     del lst[lst[2]]
#     return lst

# print(f(lst))





# lis =[1,2,4,8]
# # lis = lis[-3:-1]
# # val = lis[-4:-2]
# val1=lis[-4:-1]
# val2=lis[-2]
# val3=lis[-3]
# val4=lis[-4]
# val1=lis[-5]

# val2=lis[]
# lis = lis[-1]
# print(lis[-1])






# def fun(inp=2,out=3):
#     return inp * out

# print(fun(out=2))





# lst=[1,2]
# # val1=lst[-1]
# # val=lst[-2]
# for v in range(2):
#     lst.insert(-1,lst[v])

# print(lst)




# z=0
# y=10
# x = y<z and z>y or y>z and z<y
# print(x)


# in = a

# a =1
# b=0
# a=a^b
# b=a^b
# a=a^b

# print(a,b)
# def plus_2 (num,num2):
#     num3 = num+num2
#     return num3
#
# def minus_2 (a,b):
#     c = a-b
#     return c
#
# def multi_2 (x,y):
#     z = x*y
#     return z
#
# def divide_2 (d,j):
#      g = d // j
#      return g
#
# def pretty_print(x,opertion):
#     print("#############")
#     print(str(x) +'  The opertor is:'+ opertion)
#     print("#############")

# choose = int(input("please choose : 1 - plus , 2 - minus , 3 - Multi , 4 - divide :"))
# num = int(input("enter number:"))
# num2 = int(input("enter a second num"))
# if choose == 1:
#     res = plus_2(num,num2)
#     pretty_print(res, '+')
# elif choose == 2:
#     res = minus_2(num,num2)
#     pretty_print(res,'-')
# elif choose == 3:
#     res = multi_2(num,num2)
#     pretty_print(res,'*')
# elif choose == 4:
#     res = divide_2(num,num2)
#     pretty_print(res,'//')
# else:
#     print("invalid number")

# def even (x):
#     if x % 2 == 0:
#         print('0','even num')
#     else:
#         print('1')
#
# num = int(input("enter a number"))
# even(num)


# ls = []
# def num1 (n):
#     count = 0
#     for i in range(n):
#         b = int(input("enter a number:"))
#         ls.append(b)
#         count +=1
#     print(sum(ls)/len(ls))

# def qa3(x):
#     if x != -999:
#         for i in range (x):
#             print(len(str(x)))
#             x =input("enter a number:")
#     else:
#         print("done")

def change(x):
    changeFrom20=x//20
    print("20*",changeFrom20)
    changeFrom10=(x-(20*changeFrom20))//10
    print("10*",changeFrom10)
    changefrom5=(x-((changeFrom20*20)+(changeFrom10*10)))//5
    print("5*",changefrom5)
    changefrom1=x-((changeFrom20*20)+(changeFrom10*10)+(changefrom5*5))
    print("1*",changefrom1)
    print("--------\n",x)
change(76)

# def power(x,y):
#     c = x**y
#     return(c)

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

# def change(x):
#     changeFrom20=x//20
#     print("20*",changeFrom20)
#     changeFrom10=(x-(20*changeFrom20))//10
#     print("10*",changeFrom10)
#     changefrom5=(x-((changeFrom20*20)+(changeFrom10*10)))//5
#     print("5*",changefrom5)
#     changefrom1=x-((changeFrom20*20)+(changeFrom10*10)+(changefrom5*5))
#     print("1*",changefrom1)
#     print("--------\n",x)
#
# change(87)

# def power(x,y):
#     c = x**y
#     return(c)

# def above1000(j):
#     a = j / 100
#     c = a * 30
#     e = j - c
#     return e
#
#
# def price(x):
#     if x >1000:
#         print(above1000(x))
#     else:
#         b = x / 100
#         d = b * 10
#         r = x - d
#         print(r)

#q9
# import math
#
# def a (x,y):
#     gcd = 1
#     if x % y == 0:
#         return y
#     for i in range(int(y / 2), 0, -1):
#         if x % i == 0 and y % i == 0:
#             gcd = i
#             break
#     return gcd
#
# def b (x,y):
#     lcd = 1
#     for i in range (x,y):
#       if x % i == 0 and y % i == 0 :
#           lcd = i
#           return x
#
# def c (x,y):
#     res = x**y
#     return res
#
# def d (x,y):
#     res = math.sqrt(x)-math.sqrt(y)
#     return res
#
# num1 = int(input("enter first number:"))
# num2 = int(input("enter seconed number:"))
# choice = input("enter\n 'a' for the biggest devider\n 'b' for the smallest divider\n c for he result of pow(a,b)\n 'd' for the result of sqrt(a)-sqrt(b)\n 'e' for exit\n")
# if choice == 'a':
#     print(a(num1,num2))
# elif choice == 'b':
#     print(b(num1,num2))
# elif choice == 'c':
#     print(c(num1,num2))
# elif choice == 'd':
#     print(d(num1,num2))
# elif choice == 'e':
#     print("done")

# customerid = int(input("enter customer number:"))
# value = int (input("enter the value of the product : "))
# paidInTime = int(input("if bills paid in time enter '1' \n if not enter '0':\n"))
# numyears = int(input("enter how many years you a client :"))

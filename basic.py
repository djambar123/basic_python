# num = int(input("please enter a number:"))
# while num > 0:
#     import math
#     print(math.pow(num,2))
#     num = int(input("please enter a number:"))
# else:
#     print("invalid num")

# num = int(input("please enter your age :"))
# print('you will be',num+20,'in 20 years')

# num = int(input("please enter price to add tax :"))
# print('your price is:',(num*0.17) + num)

# num1 = int(input("enter first number:"))
# num2 = int(input("enter seconed number:"))
# plus = num1 + num2
# minus = num1 - num2
# tims = num1*num2
# mana = num1 / num2
# print (plus,minus,tims,mana)


# import time
# localtime = time.asctime(time.localtime(time.time()))
# print ("wellcome:""\n", localtime)

# num1 = int(input("enter number a:"))
# num2 = int(input("enter number b:"))
# num3 = int(input("enter number c:"))
# num4 = int(input("enter number d:"))
# print("the averege is :"num1+num2+num3+num4 /4)


# nails = int(input("how many nails:"))
# box =  nails / 40
# print (box)

# distance= int(input("enter kilomerter :"))
# speed = int(input("in what speed:"))
# time = distance / speed
# print (time)

# phone = int(input("enter phone number without 0 :"))
# num = str(int(phone))
# print("your number is:", "0" +num)


#W3RESORS

# q1
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# q2
# import sys
# print("Python version")
# print (sys.version)
# print (sys.version_info)

# q3
# import datetime
# now = datetime.datetime.now()
# print("Current date and time : ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# q4
# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# q5
# firstname = input("Input your First Name : ")
# lastname = input("Input your Last Name : ")
# print ("Hey  " + lastnamename + " " + firstnamename)

# q6
# nums = input("Input some comma seprated numbers : ")
# list =nums.split(",")
# tup = tuple(list)
# print('List : ',list)
# print('Tuple : ',tup)


# q7
# for i in range(0, 10):
#     print('*', end="")
# print("\n")
#
# q8
# num = int(input("Enter a number: "))
# sum_num = (num * (num + 1)) / 2
# print("Sum of the first", num ,"positive integers:", int(sum_num))
#
# q9
# height = float(input("Enter height in Feet: "))
# weight = float(input("Enter weight in Kilogram: "))
# print("The body mass is: ", round(weight / (height * height),2))

# q10
# for i in range(0,51):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)

# q11
# guess=int(input("guess number"))
# while guess<9 and  guess>1:
#     num=int(input("enter number"))
#     if guess==num:
#         print("well guessed")
#         guess=+1
#
# q12
# lines = []
# while True:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break;
#
# for l in lines:
#     print(l)

# q13
# color_list = ["Red", "Green", "White", "Black"]
# print((color_list[0], color_list[-1]))

# q14
# ls=[1,5,3,4,6,7,6,8]
# print(len(ls))

# q15
# list=[]
# for i in range(8):
#     x=int(input("enter number"))
#     list.append(x)
# print(list)

# q16
# list1=[1,3,4,5,6,5,5,9]
# count=0
# for i in list1:
#     if i==5:
#         count=count+1
# print(count)

# q17
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 743, 527]
#
#
# for x in numbers:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)

#q18
# ls=[1,3,4,1,5,5,6]
# for i in range(len(ls)):
#     for j in ls:
#         if ls[i]==ls[j]:
#             print(i)

#q19
# base = int(input("Input the base : "))
# height = int(input("Input the height : "))
# area = base * height / 2
# print(area)

# q20
# num = int (input("enter a number "))
# num2 = int (input("enter a second number "))
# num3 = int (input("enter a t third umber "))
# if num == num2 or num2 == num3  or num == num3:
#     sum = 0
# else:
#     sum = num + num2 + num3
# print(sum)

# q21
# def sume(x,y):
#     sum = x+y
#     if sum >15 and sum < 20:
#        sum = 20
#        return sum
#     else:
#         return sum

# q22
# def details():
#     name = "daniel"
#     age = 28
#     address = "Hadera"
#     print(name,"\n",age,"\n",address)

# q23
# x = 4
# y = 3
# z = (x + y) * (x + y)
# print(z)






# price=0
#
# hour = int (input("enter time of parking 1 - 24:"))
# yaer = input("the model of the car:")
# elct = input("is the car electric y/n: ")
#
# def dicount(a):
#     if yaer == '2022' and elct == 'y':
#         print("price before discount ","\n", a)
#         print ("after discount: ","\n" , a - (a * 0.2))
#     elif yaer == '2022':
#         print("price before discount ","\n", a)
#         print ("after discount: ","\n" , a - (a * 0.15))
#     else:
#         print("price before discount ","\n", a)
#         print ("after discount: ","\n" , a - (a * 0.10))
# # for i in range(hour):
# if hour <= 3:
#     print("the payment is : 20 ₪ per hour")
#     price = hour*20
#     dicount(price)
# elif hour > 3 and hour < 5:
#     print("the payment is : 15 ₪ per hour")
#     price = hour*15
#     dicount(price)
# elif hour > 5 and hour < 24:
#     print("the payment is : 10 ₪ per hour")
#     price = hour*10
#     dicount(price)
# else:
#     print("the payment is : 5 ₪ per hour")
#     price = hour*5
#     dicount(price)
#
#
# ticket = int(input("Enter ticket price"))
# luggage = int(input("Enter luggage kg : "))
# class_ = input("What your class: ")
#
# def dicount(b,a,c):
#     res = 0
#     if a <= 20:
#         d = b * 0.20
#         res = b - d
#         print("discount luggage of 20% =", res)
#     elif 20 < a < 40:
#         d = b * 0.25
#         res = b - d
#         print("discount luggage of 25% =", res)
#     else:
#         d = b * 0.30
#         res = b - d
#         print("discount luggage of 30% =", res)
#     if c in ("first class", "bisness"):
#         d = res * 0.05
#         res -= d
#         print("discount on class of 5% =",res)
#     else:
#         d = res * 0.01
#         res -= d
#         print("discount on class of 1% =",res)
#     return res
#
# dicount(ticket, luggage, class_)
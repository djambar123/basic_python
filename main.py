from utils import *
distance = validation(input("Enter distance to travel up until 300:"))
luggage = int(input("Enter luggage kg : "))
class_ = input("What your class: ")

ticket = int(ticketPrice(distance))
shekel = dollarToshekels(ticket)
print('price in dollar :',ticket)
print('price in shekels :',shekel)
dicount(shekel,luggage,class_)


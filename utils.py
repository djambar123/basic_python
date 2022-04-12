def dicount(t,l,c):
    res = 0
    if l <= 20:
        res = t - (t * 0.20)
        print("discount luggage of 20% =", res)
    elif 20 < l < 40:
        res = t - (t * 0.25)
        print("discount luggage of 25% =", res)
    else:
        res = t - (t * 0.30)
        print("discount luggage of 30% =", res)
    if c in ("FC", "BIS"):
        d = res * 0.05
        res -= d
        print("discount on class of 5% =",res)
    else:
        d = res * 0.01
        res -= d
        print("discount on class of 1% =",res)
    return res

def ticketPrice(a):
    if a <= 100 :
        return 100
    elif a > 100 and a <= 200 :
        return 200
    else:
        return 300

def dollarToshekels(price):
    res = price * 3.17
    return res

def loop(distance):
    while distance > 300:
        distance = validation(input("Enter distance to travel:"))
    else:
        return distance

def validation(a):
    while not a.isnumeric():
        print("invalid distance :")
        a = input("Enter another distance to travel:")
    else:
        return loop(int(a))





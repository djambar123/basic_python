from lion import Lion
from Tiger import Tiger
from Donky import Donky
from Horse import Horse

l1 = Lion("lion",True,True)
t1 = Tiger("tiger",False,True)
d1 = Donky("Donky",False,True)
h1 = Horse('Horse',True,True)


def pairing(zan1, zan2):
    if ((type(zan1).__name__ == 'Lion') and (type(zan2).__name__ == 'Tiger')) or ((type(zan1).__name__ == 'Tiger') and (type(zan2).__name__ == 'Lion')):
        if (zan1.gender == True and zan1.fertile==True) and (zan2.gender == False and zan2.fertile==True):
            baby = 'Liger'
            print(baby)
        elif (zan1.gender == False and zan1.fertile == True) and (zan2.gender == True and zan2.fertile == True):
            baby = 'Tigon'
            print(baby)
        else:
            if zan1.fertile == False or zan2.fertile == False:
                print("one is not fertile or ")
            elif (zan1.gender == False and zan2.gender == False) or (zan1.gender == True and zan2.gender == True):
                print("same gender can not reproduce")
    elif (type(zan1).__name__ == 'Donky') and (type(zan2).__name__ == 'Horse'):
        baby = 'Mule'
        print(baby)
    elif (type(zan1).__name__ == 'Lion') and (type(zan2).__name__ == 'Lion'):
        baby = "Lion cup"
        print(baby)
    elif (type(zan1).__name__ == 'Donky') and (type(zan2).__name__ == 'Donky'):
        baby = "Donkey foal"
        print(baby)
    elif (type(zan1).__name__ == 'Horse') and (type(zan2).__name__ == 'Horse'):
        baby = "Colt"
        print(baby)
    elif (type(zan1).__name__ == 'Horse') and (type(zan2).__name__ == 'Donky'):
        baby = 'Mule'
        print(baby)
    else:
        if zan1.fertile == False or zan2.fertile == False:
            print("one is not fertile or ")
        elif (zan1.gender == False and zan2.gender == False) or (zan1.gender == True and zan2.gender == True):
            print("same gender can not reproduce")

        # else:
        #     zan1,zan2.fertile == False
        #     print("one is not fertile")
        # print("invalid input")


def validtion(x, y):
    listss = ['Lion', 'Tiger', 'Horse', 'Donky']
    if (x.name or y.name) not in listss:
        print("invalid input")
    else:
        pairing(x,y)



    # elif zan1 == 'horse' and zan2 == 'donky':
    #     baby = ''
validtion(d1,h1)
from lion import Lion
from Tiger import Tiger
from Donky import Donky
from Horse import Horse

l1 = Lion("lion",False,"fertile")
t1 = Tiger("tiger",True,'fertile')
d1 = Donky("donky",False,'fertile')
h1 = Horse('horse',True,'fertile')


def pairing(zan1, zan2):
    if (type(zan1).__name__ == 'Lion') and (type(zan2).__name__ == 'Tiger'):
        if zan1.gender == True and zan2.gender == False:
            baby = 'Liger'
        elif zan1.gender == False and zan2.gender == True:
            baby = 'Tigon'
        print(baby)

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
    if



    # elif zan1 == 'horse' and zan2 == 'donky':
    #     baby = ''
pairing(l1 ,t1)
baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

code = input('Your parcel code:')

for key, value in baliky.items ():
    if key == code and value == True:
            print ('Balík byl předán kurýrovi')
            break
    elif key == code and  value == False:
            print ('Balík zatím nebyl předán kurýrovi')
            break
            
else:
    print ('Tento belik neni v zaznamu')


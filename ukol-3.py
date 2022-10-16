number = input("Please write the phone number: ")

def delka (number):
    if len (number) == 9 or len (number) == 13:
        if len (number) == 13 and number[0:4] == "+420":
            return True
        elif len (number) == 9:
            return True
        else: 
            print ("Wrong format")
    else:
        return False


print (delka(number))

message = input ('Please write you message: ')

def cena (message):
    amount_signs = len (message)
    total_messages = amount_signs//180
    if amount_signs % 180 == 0:
        return total_messages*3
    elif amount_signs < 180:
        return 3
    else:
        return total_messages*3 + 3

print (cena (message))

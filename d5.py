number = input("type :")
def change(number):
    thai = ""
    for i in range(0,len(number)):
        if number[i] == "1":
            thai += "๑" 
        elif number[i] == "2":
            thai += "๒"
        elif number[i] == "3":
            thai += "๓" 
        elif number[i] == "4":
            thai += "๔" 
        elif number[i] == "5":
            thai += "๕" 
        elif number[i] == "6":
            thai += "๖" 
        elif number[i] == "7":
            thai += "๗" 
        elif number[i] == "8":
            thai += "๘" 
        elif number[i] == "9":
            thai += "๙" 
        else:
            thai += "๐"
    return thai
thai = change(number)
print(thai)
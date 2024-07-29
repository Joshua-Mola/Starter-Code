import time

def program():
    def FtoC():
        input1 = float(input("Fahrenheit to celsius converter: "))
        result1 = float((input1 - 32) / 1.8)
        print(result1)
    def CtoF():

        input2 = float(input("Celsius to Fahrenheit converter: "))
        result2 = float(input2 * 1.8 + 32)
        print(result2)

    fr = input("From (celsius/fahrenheit): ").lower()
    if fr == "celsius":
        CtoF()
    elif fr == "fahrenheit":
        FtoC()

    time.sleep(1)

    lastInput = input("Do you want to do it again? (Y/N): ").lower()

    if lastInput == "y": 
        program()
    elif lastInput == "n":
        exit()
    else:
        print("Y or N only.")
        exit()
program()
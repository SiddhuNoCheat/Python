print("Hi This is coded by Siddhesh")

a = "place holder"
b = "place holder"


def Introduction():
    global name
    a = input("Would You Like To Give Your Name:")

    if a == "yes":
        name = input("What is your name:")
        print("Hi", name)
    elif a == "no":
        print("Ok No Problem")
    else:
        print("Pls Write yes or no")
        Introduction()


Introduction()


def raja():
    def main1():
        global a
        global b
        
        def main1div1():
            global a
            try:
                a = input("Number 1 : ")
                a = int(a)
            except ValueError:
                print((f"{a} is not an integer."))
                main1div1()
        main1div1()
        
        def main1div2():
            global b
            try:
                b = input("Number 2 : ")
                b = int(b)
            except ValueError:
                print((f"{b} is not an integer."))
                main1div2()
        main1div2()
    
    main1()
    
    def main2():
        global a
        global b
        global operation
        print("Addition")
        print("Subtraction")
        print("Multiplication")
        print("Division")
        operation = input("what do you want to do:")
        def main2Addition():
            print(f"{a} + {b} = {a+b}")
        def main2Subtraction():
            print(f"{a} - {b} = {a-b}")
        def main2Multiplication():
            print(f"{a} x {b} = {a*b}")
        def main2Division():
            print(f"{a} ÷ {b} = {a/b}")


        if operation == "Addition":
            main2Addition()
        elif operation == "Subtraction":
            main2Subtraction()
        elif operation == "Multiplication":
            main2Multiplication()
        elif operation == "Division":
            main2Division()
        else:
            print("Pls write from the given")
            main2()  
    main2() 
raja()

print("Hi This is coded by Siddhesh")

a = "place holder"
b = "place holder"

def Introduction():
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
        
def main1():
    global a
    global b
    
    def main1sub1():
        try:
            global a
            a = input("Number 1 : ")
            a = int(a)
        except ValueError:
            print((f"{a} is not an integer."))
            main1sub1()
            
            
    main1sub1()
    
    def main1sub2():
        global b
        try:
            b = input("Number 2 : ")
            b = int(a)
        except ValueError:
            print((f"{b} is not an integer."))
            main1sub2()
    
    main1sub2()

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
    if operation == "Addition":
        print(f"{a} + {b} = {a+b}")
        
main2()

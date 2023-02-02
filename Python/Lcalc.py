import math

print("Hello Friends")
print("This is a percentage calculator made by Siddhesh")
print("You know what percentage I mean ;)")

First_Name = input("First Name = ")
Second_Name = input("Second Name = ")


string = First_Name + "Friend" + Second_Name;
string = string.lower()
freq = [None] * len(string);
s = ""
tw = ""

print(string)

def mid(string):
    enum = list(enumerate(string))
    lastnum = enum[-1][0] + 1
    if lastnum % 2 == 0:
        return ""
    else:
        middle = math.floor(len(enum)/2)
        x = enum[middle][1]
        return x

for i in range(0, len(string)):  
    freq[i] = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j]):  
            freq[i] = freq[i] + 1;  
              
            #Set string[j] to 0 to avoid printing visited character  
            string = string[ : j] + '0' + string[j+1 : ];  
              
#Displays the each character and their corresponding frequency  
print("Characters and their corresponding frequencies");  
for i in range(0, len(freq)):  
    if(string[i] != ' ' and string[i] != '0'):  
        s += str(freq[i])
        print(s)

print("\n\n")

def quickmafs(string):
    global s
    global tw
    if (len(s)%2 == 0):
        print("if")
        for i in range(0, int(len(s)/2)):
            tw += str(int(s[i]) + int(s[-i]))
            print(tw)
        i = 0
        s = tw
        tw = ""
    else:
        print("else")
        for i in range(0, int(len(s)/2-0.5)):
            tw += str(int(s[i]) + int(s[-i]))
            print(tw)
        i = 0
        tw += mid(s)
        s = tw
        tw = ""

    if int(s) >= 99:
        tw = ""
        quickmafs(s)

quickmafs(s)
print(s)


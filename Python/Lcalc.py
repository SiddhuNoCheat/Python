string = "qwer";  
freq = [None] * len(string);
s = ""
tw = ""

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
#if len(s)%2 != 0:
#if "#" found with print means it was for debugging
for i in range(0, int(len(s)/2)):
    print(s)
    fn = int(s[1])
    print(s)
    print(f"")
    ln = int(s[i-1])
    print(s)
    ans = int(fn + ln)
    s = s[1:]
    print(s)
    s = s[:i-1]
    print(s)
    s += str(ans)

print(s)


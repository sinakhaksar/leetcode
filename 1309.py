
s = "10#11#12"

len = len(s)

a = ''
for i in range(len):
    lasti = s[-1 -i]
    print(lasti)
    
    if lasti == '#':
        char1 = s[-2 -i]
        char2 = s[-3 -i]
        cumbin = (char1 +char2)[::-1]
        
        print('char is ', cumbin)
        
        
print("new string is :",a)

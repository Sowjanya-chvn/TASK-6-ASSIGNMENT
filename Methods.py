def upper(a):
    i=0
    ch2=' '
    while a[i:]:
        ch=ord(a[i])
        if ch>96 and ch<123:
            ch2+=chr(ch-32)
        else:
            ch2+=chr(ch)
        i+=1
    return print("The Upper Case of the String is:",ch2)

def lower(str):
    i=0
    ch2=' '
    while str[i:]:
        ch=ord(str[i])
        if ch>64 and ch<91:
            ch2+=chr(ch+32)
        else:
            ch2+=chr(ch)
        i+=1
    return print("The Loweer Case of the String is:",ch2)

def swapcase(str):
    i=0
    ch2=' '
    while str[i:]:
        ch=ord(str[i])
        if ch>96 and ch<123:
            ch2+=chr(ch-32)
        else:
            ch2+=chr(ch+32)
        i+=1
    return print("The String is:",ch2)

def capitalize(str):
    s= ""
    for i,ch in enumerate(str):
        if(ord(ch)>=65 and ord(ch)<=90):
            s+=str[i:]
            break
        elif(ord(ch)>=97 and ord(ch)<=122):
            s+=chr(ord(ch)-32)
            s+=str[i+1:]
            break
        s+=char
    return print("The Capitalized String is:",s)

def title(a):
    s=""
    i=0
    for y in range(len(a)):
        ch=ord(a[y])
        if ch>64 and ch<91:
            s+=chr(ch+32)
        else:
            s+=chr(ch) 
    c=''
    for x in range(len(s)):
        if x==0:
            ch=ord(s[x])
            if ch>96 and ch<123:
                c+=chr(ch-32)
            else:
                c+=chr(ch)
        elif a[x-1]==' ':
            ch=ord(s[x])
            if ch>96 and ch<123:
                c+=chr(ch-32)
            else:
                c+=chr(ch)
        else:
            c+=s[x]
    print("The Title String is :",c)

def islower(b):
    for x in range(len(b)):
        ch=ord(b[x])
        if ch>=65 and ch<=90:
            return "FALSE"
            break
        else:
            continue
    return "TRUE"
        
def isupper(b):
    for x in range(len(b)):
        ch=ord(b[x])
        if ch>=97 and ch<=122:
            return "FALSE"
            break
        else:
            continue
    return "TRUE"

def isdigit(b):
    for x in range(len(b)):
        ch=ord(b[x])
        if ch>=97 and ch<=122:
            return "FALSE"
            break
        elif ch>=64 and ch<=90:
            return "FALSE"
            break   
        else:
            continue
    return "TRUE"

def isalpha(b):
    for x in range(len(b)):
        ch=ord(b[x])
        if ch>=48 and ch<=57:
            return "FALSE"
            break
        else:
            continue
    return "TRUE"

def isalnum(b):
    for x in range(len(b)):
        ch=ord(b[x])
        if ch>=97 and ch<=122:
            continue
        elif ch>=64 and ch<=90:
            continue
        elif ch>=48 and ch<=57:
            continue
        else:
            return "FALSE"
            break
    return "TRUE"


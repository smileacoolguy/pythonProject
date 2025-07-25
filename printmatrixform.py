n=10

ser= [0,1]

def fib(n):
    if n<=0:
        print("Not valid number try +ve")
        if n==0:
            ser.append(0)
            return ser
    else:
        n1,n2=0,1
        for f in range(n):
            n3=n1+n2
            ser.append(n3)
            n1,n2 = n2,n3
    return ser
print(fib(n))


def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program
for f in range(5):
    print(Fibonacci(f))
import re
I="india1 is the pakistan2"
print(I)

print([re.findall('/a/w+',x) for x in re.split(' ',I)])

hashm={"Namekey":["ismail123","456durga","vij789aya",""]}
import re
def getNum(str):
    return
def getAlp(str):
    return ''.join(re.findall('[a-zA-Z]+',str))

# lista=list(map(getAlp,hashm["Namekey"]))
# listd=list(map(getNum,hashm["Namekey"]))
import re
lista=list(map(lambda str:''.join(re.findall('\d+',str)),hashm["Namekey"]))
listd=list(map(lambda str:''.join(re.findall('[a-zA-Z]+',str)),hashm["Namekey"]))
# print(lista)
# print(listd)

x=lambda x :x.lower()

y=x("Str")
print(y)

for k,v in hashm.items():
    alpl,numl=[],[]
    for str in v:
        num=""
        alp=""
        for f in str:
            if f.isdigit():
                num=num+f
            elif f.isalpha():
                alp=alp+f
        alpl.append(alp)
        numl.append(num)
    print(numl)
    print(alpl)


i=6
for j in range(i):
    print("*"*(i-j),'{}'.format(j)*(2*j+1),"*"*(i-j),end=' ')
    print()
for j in range(i-2,-1,-1):
    print("*"*(i-j),'{}'.format(j)*(2*j+1),"*"*(i-j),end=' ')
    print()

i=6
for j in range(i):
    c=chr(65+j)
    print("#"*(i-j),'{}'.format(c)*(2*j+1),"#"*(i-j))

for j in range(i-2,-1,-1):
    c=chr(65+j)
    print("#"*(i-j),'{}'.format(c)*(2*j+1),"#"*(i-j))


i=5
j=0

pyr={"big":10,"small":5}
disp="num" #num,alp
for disp in ["num","alp"]:
    for key,val in pyr.items():
        print("Print pyramid",key)
        i=pyr[key]
        for j in range(i+1):
            for k in range(1,j+1):
                if disp == "num":
                    print(k,end=' ')
                else:
                    #print(chr(64+k), end=' ')
                    print(chr(64 + j), end=' ')
            print()
        print()

u=[]
u=u.append("u1")
u=["u2"]
print(u)

print("ism")
for j in range(7):
    for k in range(1, j + 1):
        print(chr(64 + j), end=' ')
    print()

for j in range(7):
    for k in range(1, j + 1):
        print("*", end=' ')
    print()
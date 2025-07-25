"""For given input:

dict={"names":["abc","def","xyz"],"locations":["mumbai","pune","blore"]}

Convert to output to:
dict={"names":["ABC","DEF","XYZ"],"locations":["Mumbai","Pune","Blore"]}
"""

dict={"names":["abc","def","xyz"],"locations":["mumbai","pune","blore"]}

dict["names"],dict["locations"]=list(map(lambda x: x.upper(),dict["names"])),list(map(lambda x: x.capitalize(),dict["locations"]))

print(dict)
"""Print character pyramid:
A
BB
CCC
DDDD
EEEEE
Ans: """
for j in range(7):
    for k in range(1, j + 1):
        print(chr(64 + j), end=' ')
    print()


strr = "Raivi"
dt={}
fin=[]
for f in strr:
    ctr=strr.count(f)
    if ctr not in fin:
        fin.append(ctr)
    dt[f]=ctr
print(fin)


for f in sorted(fin,reverse=True):
    for key,value in dt.items():
        if f == value:
            print(key,value)


even,odd=[],[]
for f in range(1,101):
    #print(f)
    if(f%2==0):
        even.append(f)
    else:
        odd.append(f)

# print(even)
# print(odd)

dist={}
dist['even']=even
dist['odd']=odd
print(dist)

######


class A:

    def __init__(self):
        self.lista = ["learning", "concepts", "in", "india"]
        self.listb = ["india", "romania"]

    lista = ["learning", "concepts", "in", "india"]
    listb = ["india", "romania"]



    @staticmethod
    def check(self):
        lista = ["learning", "concepts", "in", "india"]
        listb = ["india", "romania"]
        for i in lista:
            if i in listb:
                print(i)

    def check1(self):
        for i in self.lista:
            if i in self.listb:
                print(i)

    def check2(self):
        for i in A.lista:
            if i in A.listb:
                print(i)

# A.check('self')
a=A()
#a.check1()
a.check2()




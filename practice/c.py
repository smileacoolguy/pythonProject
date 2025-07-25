class C(Exception):

    #custom exception
    def __init__(self, msg):
        super().__init__(" Cust Exception " + msg)

    #singleton
    _instance = None
    def __new__(cls, msg):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def str_1(self):
        try:
            print("ajaz")
            raise C("This is wrong.")
        except C as c:
            print("Catched wrong" + str(c))


c1 = C(" This init")
C.str_1("")

c2 =C("")
print(c1 == c2)

##permutations string

from itertools import permutations
st = "ismail"
p1=permutations(st)
@staticmethod
def perm():
    for x in p1:
        tp=''.join(x)
        yield tp
shuf = perm()
print(shuf)

from collections import defaultdict
d = defaultdict(dict)
shuflist = [f for f in shuf]
for word in shuflist:
    if word in d.keys():
        d[word] = d.get(word)+1
    else:
        d.update({word:1})


print(len(d))
print(len(shuflist))

####### anagram
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
d1 = defaultdict(list)

for f in strs:
    string_itr = ''.join(sorted(f))
    d1[string_itr].append(f)
print(d1)



######## slicing and 2 way rotation
input=6
size = len(range(input))//2
lis= [ x for x in range(1,input)]
l= lis[size:]+lis[:size]

print(l)

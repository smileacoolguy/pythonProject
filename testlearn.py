


class Recursive:
    #n = int(input('number ?'))
    n=5
    def fact(self, n):
        if n == 1:
            return 1
        else:
            return n * self.fact(n - 1)

    def fact1(self, nf):
        res=1
        for f in range(nf, 1, -1):
            print(str(str(res)+"*"+str(f)))
            res = res*f
            #res1=res*
        return res



    def search(self, s, arr):
        for i in arr:
            if s == i:
                return True
            else:
                return False

    def prime(self,number):
        if number == 1 or number <=0:
            print("No prime:"+str(number))
        elif number==2:
            print("Yes prime:" + str(number))
            return {"factOfPrime": 2}
        else:
            if not (number%2==0):
                print("Yes prime:" + str(number))
                return {"factOfPrimef": r.fact(number)}
            else:
                print("No prime:" + str(number))

    def string_occ_count(self,s):
        stringmap={}
        for f in s.split():
            if f not in stringmap.keys():
                stringmap[f]=1
            else:
                stringmap[f]=stringmap.get(f)+1
        print(stringmap)
        return sorted(stringmap,reverse=False)


r = Recursive()
#print(r.fact(n))
#print(r.search(1, [1, 3, 2]))
# print("fact1")
# print(r.fact1(5))
# print(r.prime(7))
r.string_occ_count("sana is ajaz and also wife called sana but ajaz is not")

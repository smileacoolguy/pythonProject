# [1,2,3,4,5] --> 2 right rotations
# o/p: [4,5,1,2,3]


# len /2  => 2
# from median list big
#list small
# big reverse iterate
# straight iteration


def abc_test():
    input=6
    size = len(range(input))//2
    list1=[]
    list2=[]
    result=[]
    for k in range(1,input):
        if k > size:
            list1.append(k)
        else:
            list2.append(k)

    for i in list1:
        #print(i)
        result.append(i)
    for j in list2:
        #print(j)
        result.append(j)

    print(result)
#print(list1[::-1])
abc_test()



################
""" 
"This is Testing" --> string
reverse in its
place
o / p: "sihT si gnitseT"
"""


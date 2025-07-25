# from itertools import permutations
#
# i = "ismail"
#
# p = permutations(i)
#
# l=[]
# for f in p:
#     #print(f)
#     l.append(''.join(f))
#
#
# for k,f in enumerate(l):
#     if l.count(f)>1:
#         print(str(k),':',f,'||',l.count(f))
# print(set(l))
# print(len(set(l)))

def shuffle_recursive(str):
    if(len(str)<=1):
        return [str]

    combos = []
    for i, char in enumerate(str):
        word =str[:i]+str[i+1:]
        for combo in shuffle_recursive(word):
            combos.append(char + combo)

    return combos


# Test
s=shuffle_recursive("ismail")
#print(s)
print(len(s))


from collections import defaultdict
def anagrams(strs):
    anag=defaultdict(list)
    for word in strs:
        str = ''.join(sorted(word))
        anag[str].append(word)
    print(anag)
    return list(anag.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagrams(strs))
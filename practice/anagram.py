from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())


# Test it
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))


""" #without default dict
def anagrams(strs):
    #anagrams = defaultdict(list)
    anagrams= {}
    for word in strs:
        str = ''.join(sorted(word))
        if(len(anagrams)>0) and str in anagrams.keys():
            anagrams[str].append(word)
        else:
            anagrams[''.join(sorted(word))] = [''.join(sorted(word))]
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagrams(strs))
"""
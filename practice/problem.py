from typing import Dict, Any

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# [
#   ["eat", "tea", "ate"],
#   ["tan", "nat"],
#   ["bat"]
# ]

dict_anagram: dict[Any, Any] = {}

def str_check(str):
    for f in str:
       for k in dict_anagram.keys():
           if f not in k:
               return False
           # else:
           #     continue
       return True


def anagram_exist(str ):
    found = [False, None]
    for k,v in dict_anagram.items():
        for key_str in v:
            if key_str in dict_anagram:
                found = [True, k]

    if len(dict_anagram) == 0:
        liststr = []
        liststr.append(str)
        dict_anagram[str] = liststr
    else:
        if str not in dict_anagram[found[1]] and found[0] and str_check(str):
            list_f = dict_anagram[found[1]]
            list_f.append(str)
            dict_anagram[found[1]] = list_f
        else:
            list_f = dict_anagram[found[1]]
            list_f.append(str)
            dict_anagram[found[1]] = list_f


for str in strs:
    print(str)
    anagram_exist(str)
print(dict_anagram)



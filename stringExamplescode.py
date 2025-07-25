n = 10
for f in range(n):
    print('*' * f, end="")
    print('')

i = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
for k, v in i.items():
    # print(k,v)
    print(k * v, end='')
    print('')

####
a = "I am from Blore. I work in IT."
al = a.split('.')


def revs(str_s):
    res = ''
    str_ar = str_s.split(' ')
    for st in str_ar:
        res = st + " " + res
    return res


for f in al:
    if f != '':
        print(revs(f))

dict = {"names": ["abc", "def", "xyz"], "locations": ["mumbai", "pune", "blore"]}

dict["names"] = list(map(lambda x: x.title(), dict["names"]))
print(dict)

st = "ismail"
d = {}
for f in st:
    if f in d:
        d[f] += d[f]
    else:
        d[f] = 1

print(d)

even = []
odd = []
gp = {}
for f in range(100):
    if f % 2 == 0:
        even.append(f)
    else:
        odd.append(f)

gp['odd'] = odd
gp['even'] = even
print(gp)

######

str1 = 'India'
d = {}
for f in str1.lower():
    if f in d:
        d[f] += d[f]
    else:
        d[f] = 1

print(d)

k = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}


class ABC():
    def printballon(self, dct):
        for k, v in dct.items():
            #print("{}".format(k) * v)
            for f in range(v):
                print(k,end='')
            print()



a = ABC()
a.printballon(k)
print(sorted(set([f for f in 'ABBCCCDDDDEEEEE'])))

a=[]
for f in 'ABBCCCDDDDEEEEE':
    if f not in a:
        a.append(f)
print('{} : '.format(a))


class test:
    def test(self):
        integ=[]
        strr=[]
        for f in range(1001):
            ###int
            if f<100 and f>0 and f % 11 == 0:
                integ.append(f)
            if f>100 and f % 111 == 0:
                integ.append(f)

            ####str
            c = [ f1 for f1 in str(f)]
            if len(set(c)) == 1 and len(c)>1:
                #print(f)
                strr.append(f)

        print(integ)
        print(strr)

t = test()
t.test()

test.test('')

class copilot:
    def like():
        pass
    
    def dislike():
        pass


    def merge_strings(self, str1, str2):
        return str1 + str2

# Example usage:
    # Calling merge_strings from outside the class using the class name
# Calling merge_strings using a class object
obj = copilot()
result2 = obj.merge_strings("Foo", "Bar")
print(result2)  # Output: FooBar

import logging

# Configure logging to a file
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Log messages to the file
logging.info("Application started.")
logging.warning("Potential issue detected.")
logging.error("An error occurred during processing.")


class MyIterator:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

# Using the custom iterator
my_iter = MyIterator(5)
for num in my_iter:
    print(num)


def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Using the generator
for num in count_up_to(5):
    print(num)


i = 123
print(i)

ls = ["isi","iff","dadad"]
def rev(str):
    if str == str[::-1]:
        return True

for f in ls:
    if rev(f):
        print(f)

import time
from pyfiglet import Figlet

#inp=input("prompt msg:")
inp ="a"
with open('aqib.txt','w') as file:
    for i in range(100):
        #time.sleep(2)
        f = Figlet(font='slant')
        #print(f.renderText(inp))
        #print(str(i)+": My good boy"+ inp)
        file.write(str(i)+" My good boy:"+ inp+" \n")

import random
st='AJAZ'
for f in st:
    st_ch=list(st)
    random.shuffle(list(st_ch))

    print(''.join(st_ch) )

with open ('aqib.txt','r') as file:
    print(file.readlines(),end="\n")

import itertools

def get_all_substrings(s):
  """
  Generates all possible substrings (combinations of characters) of a string,
  including those with repetitions, from length 1 up to the full length of the string.

  Args:
    s: The input string.

  Returns:
    A list of all unique substrings.
  """
  all_substrings = set() # Use a set to store unique substrings automatically

  # Generate combinations of all possible lengths
  for length in range(1, len(s) + 1):
    for combination in itertools.combinations(s, length):
      all_substrings.add("".join(combination)) # Convert tuple to string and add to set

  return sorted(list(all_substrings)) # Convert set to list and sort for consistent output

# Example usage with the string "ajax"
string_to_analyze = "njbx"
result = get_all_substrings(string_to_analyze)

print(f"All unique substrings of '{string_to_analyze}':")
for sub in result:
  print(sub)
print(f"Total number of unique substrings: {len(result)}")

import itertools

def shuffle_4letter_word(input_word):
  """
  Generates all unique 4-letter words by shuffling the letters of the input word.

  Args:
    input_word: The 4-letter word to shuffle.

  Returns:
    A set of all unique 4-letter words formed by shuffling, or None if the input is not a 4-letter word.
  """

  if len(input_word) != 4:
    print("Error: Please provide a 4-letter word as input.")
    return None

  # Convert the input word to a list of characters
  letters = list(input_word)

  # Generate all permutations (shuffles) of the letters
  all_permutations = itertools.permutations(letters)

  # Store unique words in a set to avoid duplicates
  shuffled_words = set()

  # Iterate through the permutations and join the characters back into a string
  for permutation in all_permutations:
    shuffled_words.add("".join(permutation))

  return shuffled_words

# Example usage:
word = "cat"  # Example with incorrect length
result = shuffle_4letter_word(word)
if result:
  print(f"Original word: {word}")
  print(f"Shuffled words: {result}")
  print(f"Total unique shuffled words: {len(result)}")

word = "ajuz" # A 4-letter word
result = shuffle_4letter_word(word)
if result:
  print(f"\nOriginal word: {word}")
  print(f"Shuffled words: {result}")
  print(f"Total unique shuffled words: {len(result)}")



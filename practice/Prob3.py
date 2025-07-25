


def get_data():
    data = []
    #### return
    # print("type is ret")
    # for i in range(1000000):
    #     data.append(i * i)
    # return data

    ####yield
    print("type is yield")
    for i in range(1000000):
        yield i * i

    ##iter
    # def rang(n):
    #     print("type is def")
    #     for i in range(n):
    #         print(i * i)
    #     return []
    # return rang(1000000)

my_list = [1, 2, 3]
my_iterator = iter(my_list)

for f in range(len(my_list)):
    print(next(my_iterator))  # Output: 1

# print(next(my_iterator)) # This would raise StopIteration

import time


start_time = time.perf_counter()
g= get_data()
##print(g)
for f1 in g:
    # print(f1)
    pass
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.6f} seconds")


class Oops:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


o = Oops("Ismail", 1)
print(o.get_name())
o.set_name("Abhishek")
print(o.get_name())

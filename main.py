# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    evenl=[]
    oddl=[]
    fdict={}
    for f in range(0,101):
        #print(f)
        num=f/2
        if (num%2)==0:
            #print("even"+str(f))
            evenl.append(f)
        else:
            #print("odd"+str(f))
            oddl.append(f)
    fdict['evenN']=evenl
    fdict['oddN']=oddl
    print(fdict)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

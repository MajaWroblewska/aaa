# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from string import ascii_lowercase, ascii_uppercase, ascii_letters


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    # print_hi('PyCharm')

    # zam= random.sample((ascii_lowercase), k=4)
    # lp = random.randint(0,9)
    lista=list(ascii_letters)+[str(x) for x in range(10)]
    print(lista)
    mix= random.sample(lista, k=8)
    # print(mix)
    print("".join(mix))
    print('-'*50)

    import datetime
    x = datetime.datetime.now()
    print(x)

    dz = [str(x.year),str(x.month),str(x.day),]
    go= [str(x.hour), str(x.minute), str(x.second)]
    d='/'.join(dz)
    g=''.join(go)
    zamowienie= d +"/"+g
    print(zamowienie)
















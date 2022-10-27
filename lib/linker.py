import sys
import merger
from os import remove
from shutil import copyfile

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def newlist(name, data, n):
    nl = open(f"../data/{name}", "w")
    for z in range(n):
        nl.write(data)
    nl.close()

def endStore(a, b):
    storefile = open("../data/status", "w")
    storefile.write(f"{a}\n")
    storefile.write(f"{b}")
    storefile.close()
    sys.exit()

storing = open("../data/status", "r")
datum = storing.readlines()
first = int(datum[0])
second = int(datum[1])

origlist = open("../data/list", "r")
datas = origlist.readlines()
length = len(datas)
if length % 2 != 0:
    datas.append("[bad holder]")
    length = len(datas)

for x in range(1, length + 1):
    newlist(f"list{x}", datas[x - 1], 1)

for i in range(first, int(length / 2)):
    rem = length % (2 * i)
    if rem != 0:
        num = 2 ** (i - 1)
        newlist(f"list{length - rem + 1}", "[bad holder]", num) 
    for j in range(second, length + 1, 2 * i):
        print(j)
        print(j + (2 ** (i - 1)))
        merger.init(j, j + (2 ** (i - 1)))
        cont = input("Continue? (Y/n) ")
        if cont == "n":
            endStore(i, j)


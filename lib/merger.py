import sys
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

def init(a, b):
    global firstnumber
    global secondnumber
    global firstlist
    global secondlist
    global stat

    firstnumber = int(a)
    secondnumber = int(b)
    firstlist = f"list{firstnumber}"
    secondlist = f"list{secondnumber}"
    storefile = open("../data/store", "r")
    stat = 0

    print(firstlist)
    print(secondlist)
    
    if int(storefile.readlines()[0]) == 0:
        copyfile(f"../data/{firstlist}", f"../data/fl")
        copyfile(f"../data/{secondlist}", f"../data/sl")
    else:
        pass

    next()
    return

def removeLine(listname):
    copyingfile = open(f"../data/{listname}copy", "w")
    with open(f"../data/{listname}", "r") as rf:
        copylines = rf.readlines()
        length = len(copylines)
        rf.close()
    copiedlines = []
    for i in range(1, length):
        copiedlines.append(copylines[i])
    for j in range(length - 1):
        copyingfile.write(copiedlines[j])
    copyingfile.close()
    remove(f"../data/{listname}")
    copyfile(f"../data/{listname}copy", f"../data/{listname}")
    remove(f"../data/{listname}copy")

def endStore(i):
    storefile = open("../data/store", "w")
    storefile.write(f"{i}")
    storefile.close()
    global stat
    stat = 1
    return

def mergeSort():
    with open(f"../data/{firstlist}", "r") as f1:
        datas = f1.readlines()
        try:
            first1 = datas[0]
        except IndexError:
            first1 = " "
        f1.close()
    with open(f"../data/{secondlist}", "r") as f2:
        datas = f2.readlines()
        try:
            first2 = datas[0]
        except IndexError:
            first2 = " "
        f2.close()
    print(color.BOLD + first1 + color.END)
    print(color.BOLD + first2 + color.END)
    vote = input("Vote: ")
    if vote == "1":
        finalfile.write(first1)
        removeLine(firstlist)
    elif vote == "2":
        finalfile.write(first2)
        removeLine(secondlist)
    elif vote == "end":
        endStore(1)
    elif vote == "reset":
        remove(f"../data/{firstlist}")
        remove(f"../data/{secondlist}")
        copyfile("../data/fl", f"../data/{firstlist}")
        copyfile("../data/sl", f"../data/{secondlist}")
        remove(f"../data/fl")
        remove(f"../data/sl")
        endStore(0)
    elif vote == "done":
        remove(f"../data/{firstlist}")
        remove(f"../data/{secondlist}")
        copyfile("../data/wlist", f"../data/{firstlist}")
        endStore(1)
    else:
        pass

def next():
    x = 1
    global finalfile
    copyfile("../data/wlist", "../data/listcopy")
    copyingfile = open("../data/listcopy", "r")
    cplines = copyingfile.readlines()
    cplength = len(cplines)
    copyingfile.close()
    finalfile = open("../data/wlist", "w")
    for a in range(cplength):
        finalfile.write(cplines[a])
    remove("../data/listcopy")
    while x == 1:
        if stat == 0:
            mergeSort()
        elif stat == 1:
            return
    

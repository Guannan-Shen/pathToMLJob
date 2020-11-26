# find all methods
# dir(list)

# help(list.append)
# help(list.extend)

# compare memory location
lst1 = [1, 2, 3]
print(id(lst1))
lst2 = lst1
print(id(lst2))
lst1.count(1)


lst1.append(4)
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))

# + sign
lst1 = lst1 + [5]
print(lst1)
print(lst2)
print("Compare memory location ID", id(lst1) == id(lst2))
print(id(lst1))
print(id(lst2))

# slicing 
print("Compare memory location ID", id(lst1) == id(lst1[:]))

# string 
h = "Hello World"
print(h[:10000])

print(h.lower())

for i in range(0, 9, 2):
    print(i)

S = ['a', 'b', 'c']
for item in S:
    print(item*2)

L = [1, 2, 3]
newLst = []
for item in L:
    newLst.append(item*2)

print(newLst)

for item in L:
    item = item*2
print(L)

for i in range(len(L)):
    L[i] = L[i]*2
print(L)


dir(str)

# typing
from typing import List, Dict, TextIO


# list
# List[str]
# use type hints as precise as possible 
# List[float]
# tuple[tuple[str, int], dict[str, str]]

# test whether it is a numeric or not 
test_string = "3.1415926"
t2 = "3"
test_string.isnumeric()
test_string.replace('.', '', 1).isnumeric()
t2.isnumeric()

print([1,2,3].append('eye'))
lst_t = [1,2,3].append('eye')
print(lst_t)


lst1 = [1, 2, 3]
lst_t2 = lst1.append('eye')
print(lst_t2)
print(lst1)

# negative infinity
float('-inf')

# 

# readfile
# \n at the end, counted as a character
f = open('test_readline.txt' , 'r')
if len(f.readline()) == 6:
    # the next line 
    print(f.readline())
print(len(f.readline()))

f.close()

f = open('test_readline.txt' , 'r')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()


f = open('test_readline.txt' , 'r')
for line in f.readlines():
    line = line.strip()
    print(line)
f.close()

def second_function(s):
    while len(s) < 10:
        s = s + s
    return s

second_function("Hel")

S = "sb"
S = S + S
print(S)


def first_function(values):
    n = len(values)
    for i in range(n):
        values[i], values[n - 1 - i] = values[n - 1 - i], values[i]
print(lst1)
first_function(lst1)
print(lst1)
print(first_function(lst1))

from typing import List, Callable
def third_function(L: List[int], f:Callable):
    for n in L:
        n = f(n)

L = [-2, 1, -3]
print(third_function(L, abs))
print(L)


from typing import TextIO

def convert_int(year:int, label:str) -> int:
    if label == "AD":
        return int(year)
    elif label == "BC":
        return -int(year)

def get_year_diff_file(data_file: str, year_file: str) -> None:
    f = open(data_file, "r")
    w = open(year_file, "w")
    for line in f:
        line = line.strip().split()
        y1 = convert_int(line[0], line[1])
        y2 = convert_int(line[2], line[3])
        diff = abs(y1 - y2)
        w.write(str(diff) + '\n')
    w.close()
    f.close()

get_year_diff_file("year.txt", "diff.txt")


def get_year_diff_file(data_file: TextIO, year_file: TextIO) -> None:
    for line in data_file:
        line = line.strip().split()
        y1 = convert_int(line[0], line[1])
        y2 = convert_int(line[2], line[3])
        diff = abs(y1 - y2)
        year_file.write(str(diff) + '\n')

f = open("year.txt", 'r')
w = open("diff2.txt", 'w')
get_year_diff_file(f, w)
f.close()
w.close()


def total_nums(los: list):
    """
    Returns the total number of 
    strings that in list <los> that 
    contains only numeric digits.
    
    >>> total_nums([])
    0
    >>> total_nums(["12", "ab", "a12", "omg", "250"])
    2
    """
    acc = 0
    for s in los:
        if s.isdigit():
            acc += 1
    return acc


# test TextIO
from typing import TextIO

with open("numbers.txt", 'w') as writer:
    for i in range(1, 1001):
        writer.write(str(i) + '\n')


with open('numbers.txt', 'r') as f:
    x = 0
    for line in f:
        num = int(line.strip())
        x = x + num
    print(x)
    x = 0
    for line in f:
        num = int(line.strip())
        x = x + 1
    print(x)

f = open('numbers.txt')
x = 0
for line in f:
    num = int(line.strip())
    x = x + 1
print(num)
print(x)
f.close()

f = open('numbers.txt')
x = 0
for line in f:
    line = f.readline()
    num = int(line.strip())
    x = x + 1
print(num)
print(x)
f.close()

f = open('numbers.txt')
x = 0
for line in f:
    line = f.readline()
    num = int(line.strip())
    if num % 2 == 1:
        x = x + 1
print(num)
print(x)
f.close()

f = open('numbers.txt')
x = 0
for line in f:
    num = int(line.strip())
    if num % 100 == 0:
        x = x + 1
print(num)
print(x)
f.close()


from typing import List
def f(n: int, m: int) -> List[int]:
    result = []
    for i in range(n):
        for j in range(n + m):
            if (j % 2 == 0):
                result.append(1)
            elif (i % 2 == 0):
                result.append(2)
            else:
                result.append(0)
    return result

print(f(2, 0))
print(f(1, 5))
import random
import datetime

Names        = 'Data/Names.txt'
MiddleNames  = 'Data/MiddleNames.txt'
SurNames     = 'Data/Surnames.txt'
TownNames    = 'Data/TownNames.txt'
CompanyNames = 'Data/CompanyNames.txt'



def Number(start=0, end=100):
    return random.randint(start, end)


def rawCount(filename):
    with open(filename, 'rb') as f:
        lines = 1
        buf_size = 1024 * 1024
        read_f = f.raw.read

        buf = read_f(buf_size)
        while buf:
            lines += buf.count(b'\n')
            buf = read_f(buf_size)
        return lines


def randomLine(filename):
    num = int(random.uniform(0, rawCount(filename)))
    with open(filename, 'r', encoding="UTF-8") as f:
        for i, line in enumerate(f, 1):
            if i == num:
                break
    return line.strip('\n')


def First():
    return randomLine(Names)


def Last():
    return randomLine(SurNames)


def Middle():
    return randomLine(MiddleNames)

from random import randrange
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.days
    random_days = randrange(int_delta)
    return start + timedelta(seconds=random_days)

def birthday():
    d1 = datetime.strptime('1/1/1945', '%d/%m/%Y')
    d2 = datetime.strptime('1/1/2004', '%d/%m/%Y')
    d = str(random_date(d1, d2))
    return d[:10]

def telephone():
    return str(random.randint(123456, 999999))


def Company():
    return randomLine(CompanyNames)


def Town():
    _Cc = randomLine(TownNames)
    return _Cc[3:]


def Full():
    return ' '.join([First(), Middle(), Last()])


def filename():
    return "data.txt"

with open (filename(),"w") as file:
    for i in range(10):
        file.write(str(i) + "," +  Full() + "," + birthday() + "," + Company() + "," + Town() + "," + telephone() + "\n")
        





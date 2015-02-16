import urllib2
import re
import datetime

from multiprocessing import Pool
from bs4 import BeautifulSoup

def convertme(instr):
    instr = instr[:-6]
    instr = instr.replace("T", " ")
    tmp = re.findall(r"[\w]+", instr)
    tmp = map(int, tmp)
    outdate = datetime.datetime(*tmp)
    outdate += datetime.timedelta(hours=3)
    return outdate

def get_times(page):
    heap = []

    tmpurl = "http://www.dotabuff.com/players/114001493/matches?page=" + str(page)

    #response = urllib2.urlopen(tmpurl, timeout=10)
    x = urllib2.Request(tmpurl, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(x)
    html = response.read()

    soup = BeautifulSoup(html)
    mylist = soup.find_all("time")
    del mylist[0]
    for i in mylist:
        heap.append(i['datetime'])
    heap = map(convertme, map(str, heap))
    heapofdays = []
    for d in heap:
        heapofdays.append(d.date())
    heapofdays = (map(str, heapofdays))

    return heapofdays


pool = Pool(processes = 4)
print pool.map(get_times, range(170))


import urllib2
import re
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bs4 import BeautifulSoup


def index(request):
    return HttpResponse("Hello, world. You're at the grabdatax root.")


def goto(request):
    # return HttpResponse("goto")
    return render(request, 'grabdatax/goto.html')


@csrf_exempt
def list(request):
    # a = 5
    # return HttpResponse("goto")
    # x = urllib2.Request("http://www.dotabuff.com/players/114001493/matches?page=2",
    #                     headers={'User-Agent': 'Mozilla/5.0'})
    # response = urllib2.urlopen(x)
    # html = response.read()

    # myheap = []
    # for i in range(1, 50):
    #     myheap.append(get_times("http://www.dotabuff.com/players/114001493/matches?page=", i))

    # mytimes = get_times("http://www.dotabuff.com/players/114001493/matches?page=", 2)

    # return HttpResponse(' '.join(str(myheap)))
    with open('test.txt', 'w') as outfile:
        outfile.write("PUT TEXT!")
    return HttpResponse("xex")

    # return render(request, 'grabdatax/list.html')


def get_times(url, page):
    heap = []

    tmpurl = url + str(page)

    # response = urllib2.urlopen(tmpurl, timeout=10)
    x = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
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


def convertme(instr):
    instr = instr[:-6]
    instr = instr.replace("T", " ")
    tmp = re.findall(r"[\w]+", instr)
    tmp = map(int, tmp)
    outdate = datetime.datetime(*tmp)
    outdate += datetime.timedelta(hours=3)
    return outdate
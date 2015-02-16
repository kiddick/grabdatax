import urllib2
import requests
import re
import datetime

import threading
import Queue

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

    #myheap = []
    #for i in range(1, 176):
    #    myheap.append(get_times("http://www.dotabuff.com/players/114001493/matches?page=", i))

# LAST    myheap = getTimesRequest("http://www.dotabuff.com/players/114001493/matches?page=", 176)

    #mytimes = get_times("http://www.dotabuff.com/players/114001493/matches?page=", 2)
    fetch_parallel()

#LAST    return HttpResponse(' '.join(str(myheap)))


    return HttpResponse('DONE!')
    #with open('test.txt', 'w') as outfile:
    #    outfile.write("PUT TEXT!")
    #return HttpResponse("xex")

    # return render(request, 'grabdatax/list.html')

buff = []
for i in range(1, 170):
    buff.append('http://www.dotabuff.com/players/114001493/matches?page=' + str(i))

def read_url(url, queue):
    x = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib2.urlopen(x).read()
    print('Fetched %s from %s' % (len(data), url))
    with open('outspeed.html', 'a') as outfile:
	outfile.write(data)
    queue.put(data)

def fetch_parallel():
    result = Queue.Queue()
    threads = [threading.Thread(target=read_url, args = (url,result)) for url in buff]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return result

def fetch_sequencial():
    result = Queue.Queue()
    for url in buff:
        read_url(url,result)
    return result

def getTimesRequest(url, page):
    heapofdays = []
    heap = []
    session = requests.Session()
    for i in range(1, page):
	headers = {'User-Agent' : 'Mozilla/5.0'}
	r = session.get(url + str(i), headers = headers)
	html = r.content
	#soup = BeautifulSoup(html)
	#mylist = soup.find_all("time")
	#del mylist[0]
	#for j in mylist:
    	    #heap.append(j['datetime'])
	#heapofdays = []
	heapofdays.append(str(html))
	with open('out.html', 'w') as outf:
	    outf.write('\n'.join(heapofdays))
    #heap = map(convertme, map(str, heap))
    #heapofdays = []
    #for d in heap:
        #heapofdays.append(d.date())
    #heapofdays = (map(str, heapofdays))

    #return page
    return len(heapofdays)
    #return heapofdays



def get_times(url, page):
    heap = []

    tmpurl = url + str(page)

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


def convertme(instr):
    instr = instr[:-6]
    instr = instr.replace("T", " ")
    tmp = re.findall(r"[\w]+", instr)
    tmp = map(int, tmp)
    outdate = datetime.datetime(*tmp)
    outdate += datetime.timedelta(hours=3)
    return outdate
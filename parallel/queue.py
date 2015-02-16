import threading, urllib2
import Queue
import cProfile

urls_to_load = [
'http://stackoverflow.com/',
'http://slashdot.org/',
'http://www.archive.org/',
'http://www.yahoo.co.jp/',
]

    # x = urllib2.Request(tmpurl, headers={'User-Agent': 'Mozilla/5.0'})
    # response = urllib2.urlopen(x)
    # html = response.read()

buff = []
for i in range(1, 1001):
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

#cProfile.run('fetch_sequencial()')
cProfile.run('fetch_parallel()')
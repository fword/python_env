import sys,os
import urllib,urllib2
import traceback
def quchong(mylist):
    aa=set()
    for item in mylist:
        aa.add(item.strip())
    return list(aa)
def filediff(file1,file2):
    aa=set()
    bb=set()
    for item in open(file1):
        aa.add(item.strip())
    for item in open(file2):
        bb.add(item.strip())
    if len(aa)>len(bb):
        return list(aa-bb)
    else:
        return list(bb-aa)
def _download(filename,url):
    for i in range(3):
        try:
            urllib.urlretrieve(url,filename)
            break
        except:
            print traceback.print_exc()
            pass
def muti_xiecheng_download(filename):
    import socket
    from gevent import monkey
    monkey.patch_all(dns=False)
    import gevent
    from gevent.queue import Queue
    socket.setdefaulttimeout(5)
    tasks = Queue()
    def worker(num):
        while not tasks.empty():
            task = tasks.get()
            tasklist=task.split('\t')
            if len(tasklist)!=2:
                continue
            filen=tasklist[0].strip()
            urln=tasklist[1].strip()
            _download(filen,urln)
            gevent.sleep(0)
    def boss(filename):
        for line in open(filename):
            line=line.strip()
            tasks.put_nowait(line)
    gevent.spawn(boss,filename).join()
    threads = [gevent.spawn(worker,i) for i in range(100)]
    gevent.joinall(threads)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
def urlopen(url,trytimes=3,timeout=5,headers=headers):
    for i in range(trytimes):
        try:
            request = urllib2.Request(url=url,headers=headers)
            response = urllib2.urlopen(request, timeout=timeout)
            return response.read()
        except:
            pass
def urlstore(url,filename,trytimes=3,timeout=5):
    import socket
    socket.setdefaulttimeout(timeout)
    for i in range(trytimes):
        try:
            urllib.urlretrieve(url,filename)
            return 1
        except:
            pass
    return 0


import sys,os
import urllib
import traceback
def quchong(mylist):
    aa=set()
    for item in mylist:
        aa.add(item.strip())
    return list(aa)
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
def _is_real_pic(filename):
    import cv2
    try:
        ret=cv2.imread(filename)
        if ret is None: 
            return 0
        else:
            return 1
    except:
        return 0
    return 0
def del_pic_trash(mydir):
    for root,dirfile,filelist in os.walk(mydir):
        for fileone in filelist:
            file=os.path.join(root,fileone)
            if not _is_real_pic(file):
                os.remove(file)

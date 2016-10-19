import sys,os
import traceback
import cv2
def _is_real_pic(filename):
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

#-*- coding:UTF-8 -*-
import requests,re, json, sys
from urllib import request


def Schedule(self, a, b, c):
        per = 100.0*a*b/c
        if per > 100 :
            per = 1
        sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per,a*b,c) + '\r')
        sys.stdout.flush()

def video_download(self, url, filename):
    request.urlretrieve(url=url,filename=filename,reporthook=self.Schedule)

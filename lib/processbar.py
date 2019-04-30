#!/usr/bin/python
# -*- coding: UTF-8 -*-

import platform
from tqdm import tqdm

class DummyFile(object):
  file = None
  def __init__(self, file):
    self.file = file

  def write(self, x):
    if len(x.rstrip()) > 0:
        tqdm.write(x, file=self.file)



class ProcessBar:
    def __init__(self,total):
        if platform.system()=="windows":
            self.pbar = tqdm(total=total,ascii=True)
        else:
            self.pbar = tqdm(total=total)

        self.cur_cnt = 0
        self.suc_cnt = 0
        self.total = total

    def update(self,n):
        self.pbar.update(n)
        self.cur_cnt +=1

    def echo(self,msg):
        self.pbar.write(str(msg))


    def close(self):
        self.pbar.close()


if __name__ == '__main__':
    from time import sleep
    pbar = ProcessBar(50)
    for i in range(50):

        pbar.echo(i)
        pbar.update(1)
        sleep(.1)
    pbar.close()
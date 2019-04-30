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
        if platform.system()=="Windows":
            self.pbar = tqdm(total=total,ncols=80,bar_format='{l_bar}{bar}|{postfix}/{n_fmt}/{total_fmt} [{elapsed}<{remaining},''{rate_fmt}{postfix}]')
        else:
            self.pbar = tqdm(total=total,bar_format='{l_bar}{bar}|{postfix}/{n_fmt}/{total_fmt} [{elapsed}<{remaining},''{rate_fmt}{postfix}]')

        self.cur_cnt = 0
        self.suc_cnt = 0
        self.total = total

    def update(self):
        self.pbar.update(1)
        self.cur_cnt +=1

    def update_suc(self):
        self.suc_cnt +=1
        self.pbar.postfix = self.suc_cnt

    def echo(self,msg):
        self.pbar.write(msg)


    def close(self):
        self.pbar.close()


if __name__ == '__main__':
    from time import sleep
    pbar = ProcessBar(10)
    for i in range(10):
        pbar.echo(u"张三")
        pbar.update(1)
        sleep(.1)
    pbar.close()
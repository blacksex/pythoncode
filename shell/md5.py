#coding : utf-8
import hashlib
import os
class md5js:
 def md5sum(self,fname):
    """
    计算文件的MD5值
    """
    m = hashlib.md5()
    with open(fname,'rb') as fh:
        for chunk in read_chunks(fh):
            m.update(chunk)
    return m.hexdigest()

def read_chunks(self,fh):
    fh.seek(0)
    chunk = fh.read(8096)
    while chunk:
        yield chunk
        chunk = fh.read(8096)
    else: #最后要将游标放回文件开头
        fh.seek(0)